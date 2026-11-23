"""Pruebas unitarias del ejemplo de autenticación."""
import unittest

from autenticacion_estrategia import (
    AuthenticationService,
    InMemorySessionManager,
    PasswordAuthenticationStrategy,
    UserAccount,
    create_password_digest,
)


class FakeUserRepository:
    def __init__(self, account: UserAccount) -> None:
        self.account = account

    def find_by_email(self, email: str) -> UserAccount | None:
        if email == self.account.email:
            return self.account
        return None


class AuthenticationStrategyTests(unittest.TestCase):
    def setUp(self) -> None:
        account = UserAccount(
            user_id="est-001",
            email="estudiante@ejemplo.edu.do",
            role="estudiante",
            active=True,
            password=create_password_digest("Clave-de-prueba-2026"),
        )
        self.repository = FakeUserRepository(account)
        self.sessions = InMemorySessionManager()
        strategy = PasswordAuthenticationStrategy(self.repository)
        self.service = AuthenticationService(strategy, self.sessions)

    def test_valid_credentials_create_a_session(self) -> None:
        result = self.service.login(
            " ESTUDIANTE@EJEMPLO.EDU.DO ",
            "Clave-de-prueba-2026",
        )
        self.assertIsNotNone(result)
        assert result is not None
        self.assertEqual(
            self.sessions.user_id_for(result.access_token),
            "est-001",
        )

    def test_wrong_password_is_rejected(self) -> None:
        result = self.service.login(
            "estudiante@ejemplo.edu.do",
            "contraseña-incorrecta",
        )
        self.assertIsNone(result)

    def test_inactive_account_is_rejected(self) -> None:
        self.repository.account = UserAccount(
            user_id="est-001",
            email="estudiante@ejemplo.edu.do",
            role="estudiante",
            active=False,
            password=self.repository.account.password,
        )
        result = self.service.login(
            "estudiante@ejemplo.edu.do",
            "Clave-de-prueba-2026",
        )
        self.assertIsNone(result)

    def test_logout_revokes_the_session(self) -> None:
        result = self.service.login(
            "estudiante@ejemplo.edu.do",
            "Clave-de-prueba-2026",
        )
        assert result is not None
        self.service.logout(result.access_token)
        self.assertIsNone(self.sessions.user_id_for(result.access_token))


if __name__ == "__main__":
    unittest.main()
