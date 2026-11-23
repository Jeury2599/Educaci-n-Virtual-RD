"""Ejemplo de referencia para el inicio de sesión de Educación Virtual RD.

El módulo demuestra el patrón Strategy y un manejo básico de sesiones opacas.
No es un servidor web ni sustituye una base de datos de producción.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import secrets
import time
from typing import Protocol


PBKDF2_ITERATIONS = 600_000


@dataclass(frozen=True)
class PasswordDigest:
    salt: bytes
    digest: bytes


@dataclass(frozen=True)
class UserAccount:
    user_id: str
    email: str
    role: str
    active: bool
    password: PasswordDigest


@dataclass(frozen=True)
class AuthenticatedUser:
    user_id: str
    email: str
    role: str


@dataclass(frozen=True)
class AuthenticationResult:
    user: AuthenticatedUser
    access_token: str


def create_password_digest(password: str) -> PasswordDigest:
    """Genera un hash con sal aleatoria; nunca guarda la contraseña original."""
    if not password:
        raise ValueError("La contraseña no puede estar vacía.")

    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        PBKDF2_ITERATIONS,
        dklen=32,
    )
    return PasswordDigest(salt=salt, digest=digest)


def verify_password(password: str, stored: PasswordDigest) -> bool:
    """Compara el hash calculado con el almacenado, sin revelar la contraseña."""
    candidate = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        stored.salt,
        PBKDF2_ITERATIONS,
        dklen=32,
    )
    return hmac.compare_digest(candidate, stored.digest)


class UserRepository(Protocol):
    def find_by_email(self, email: str) -> UserAccount | None:
        """Busca una cuenta por correo normalizado."""
        ...


class AuthenticationStrategy(Protocol):
    def authenticate(
        self, email: str, password: str
    ) -> AuthenticatedUser | None:
        """Devuelve un perfil seguro o None si no se puede autenticar."""
        ...


class PasswordAuthenticationStrategy:
    """Estrategia actual: autenticación local mediante correo y contraseña."""

    def __init__(self, users: UserRepository) -> None:
        self._users = users

    def authenticate(
        self, email: str, password: str
    ) -> AuthenticatedUser | None:
        normalized_email = email.strip().lower()
        if not normalized_email or not password:
            return None

        account = self._users.find_by_email(normalized_email)
        if account is None or not account.active:
            return None

        if not verify_password(password, account.password):
            return None

        # No se devuelve el hash ni la sal al resto de la aplicación.
        return AuthenticatedUser(
            user_id=account.user_id,
            email=account.email,
            role=account.role,
        )


class SessionManager(Protocol):
    def create(self, user_id: str) -> str:
        ...

    def user_id_for(self, token: str) -> str | None:
        ...

    def revoke(self, token: str) -> None:
        ...


class InMemorySessionManager:
    """Adaptador didáctico: guarda el hash del token en memoria.

    En producción debe sustituirse por un almacén persistente y compartido,
    con expiración, revocación y controles de acceso.
    """

    def __init__(self, ttl_seconds: int = 900) -> None:
        if ttl_seconds <= 0:
            raise ValueError("La duración de la sesión debe ser positiva.")
        self._ttl_seconds = ttl_seconds
        self._sessions: dict[bytes, tuple[str, float]] = {}

    @staticmethod
    def _token_digest(token: str) -> bytes:
        return hashlib.sha256(token.encode("utf-8")).digest()

    def create(self, user_id: str) -> str:
        token = secrets.token_urlsafe(32)
        digest = self._token_digest(token)
        self._sessions[digest] = (
            user_id,
            time.monotonic() + self._ttl_seconds,
        )
        return token

    def user_id_for(self, token: str) -> str | None:
        if not token:
            return None

        digest = self._token_digest(token)
        record = self._sessions.get(digest)
        if record is None:
            return None

        user_id, expires_at = record
        if time.monotonic() >= expires_at:
            self._sessions.pop(digest, None)
            return None

        return user_id

    def revoke(self, token: str) -> None:
        if token:
            self._sessions.pop(self._token_digest(token), None)


class AuthenticationService:
    """Coordina la estrategia elegida y la creación de la sesión."""

    def __init__(
        self,
        strategy: AuthenticationStrategy,
        sessions: SessionManager,
    ) -> None:
        self._strategy = strategy
        self._sessions = sessions

    def login(
        self, email: str, password: str
    ) -> AuthenticationResult | None:
        user = self._strategy.authenticate(email, password)
        if user is None:
            return None

        token = self._sessions.create(user.user_id)
        return AuthenticationResult(user=user, access_token=token)

    def logout(self, token: str) -> None:
        self._sessions.revoke(token)
