# Ingeniería de Software II - Intervención del componente de autenticación

## Componente seleccionado

Se seleccionó el inicio de sesión y control de acceso de Educación Virtual RD. Es una función central porque estudiantes, docentes y administradores necesitan identificarse antes de entrar a las áreas privadas de la plataforma.

En la versión documental inicial, el diagrama de secuencia mostraba una pantalla que enviaba el correo y la contraseña a un único Servicio de autenticación. Este servicio consultaba la base de datos y verificaba las credenciales y el estado de la cuenta. El flujo estaba descrito, pero no separaba la forma de autenticación ni definía el manejo de una sesión después del acceso.

## Limitación encontrada

El diseño dejaba la validación de credenciales dentro de un solo servicio. Si más adelante se quisiera añadir acceso institucional u otro proveedor de identidad, habría que modificar esa parte central. También faltaba representar con claridad la diferencia entre los datos privados de la cuenta y el perfil seguro que el resto de la aplicación necesita.

La documentación inicial ya indicaba que las contraseñas no debían guardarse en texto plano y que las rutas privadas debían comprobar permisos, pero no mostraba una estructura de clases para aplicar esas reglas.

## Patrón seleccionado: Strategy (Estrategia)

Se eligió el patrón de comportamiento Strategy. La idea es definir una interfaz común para autenticar y permitir que cada método tenga su propia implementación. El servicio principal no necesita conocer los detalles de cada método; trabaja con la interfaz.

Para esta etapa se implementa como referencia la estrategia local de correo y contraseña. En otra etapa podría añadirse una estrategia de autenticación institucional u OAuth sin rehacer el servicio que coordina el inicio de sesión.

## Diseño propuesto

- **AuthenticationService:** recibe la solicitud y coordina el proceso.
- **AuthenticationStrategy:** contrato común para las formas de autenticación.
- **PasswordAuthenticationStrategy:** valida el correo, el estado de la cuenta y la contraseña.
- **UserRepository:** obtiene los datos de la cuenta sin exponer la base de datos al servicio.
- **SessionManager:** crea, valida y revoca la sesión después de autenticar.
- **Frontend / API:** recibe las credenciales por HTTPS y devuelve una respuesta sin incluir hashes ni sales.

El diagrama de esta carpeta representa la relación entre estos elementos y el flujo de una solicitud.

## Cambios realizados en el ejemplo de referencia

Se añadieron los archivos `autenticacion_estrategia.py` y `test_autenticacion_estrategia.py`.

La estrategia local:
1. Normaliza el correo recibido.
2. Busca la cuenta mediante el repositorio.
3. Rechaza cuentas inexistentes o inactivas.
4. Verifica la contraseña comparando el hash calculado con el guardado.
5. Devuelve un perfil reducido, sin sal ni hash.

El servicio principal recibe la estrategia por el constructor. Después de autenticar, solicita al administrador de sesiones un token opaco aleatorio. El ejemplo guarda únicamente el hash SHA-256 del token en memoria, permite comprobar su vigencia y lo revoca al cerrar sesión. Las pruebas verifican el acceso correcto, el rechazo de una contraseña incorrecta, el rechazo de una cuenta inactiva y el cierre de sesión.

## Credenciales y tokens

La contraseña se recibe solo para validar el acceso. No se guarda ni se devuelve. La cuenta conserva una sal aleatoria y el resultado de una función de derivación de clave. El ejemplo usa PBKDF2-HMAC-SHA-256 con 600,000 iteraciones; OWASP recoge ese valor para PBKDF2-HMAC-SHA-256 cuando se necesita esta alternativa. Para un despliegue real se debe evaluar Argon2id como primera opción, revisar los requisitos del entorno y ajustar los parámetros con pruebas.

El token de sesión del ejemplo es opaco: no contiene el correo ni el rol del usuario y no es un JWT. Se genera con un generador criptográfico, se entrega al cliente y el servidor conserva su hash con una fecha de expiración. Al cerrar sesión se elimina el registro. En una aplicación web real, la API debe enviarlo en una cookie con `Secure`, `HttpOnly`, `SameSite` y alcance limitado. No debe almacenarse en `localStorage` o `sessionStorage`. La sesión debe caducar y poder revocarse en el servidor.

## Alcance y limitaciones de la intervención

El repositorio original contiene análisis, requisitos, arquitectura y modelos UML; no contiene una aplicación web desplegada ni una base de datos conectada. Por esa razón, el código añadido es una implementación de referencia ejecutable y comprobable de la lógica del componente, no una integración de producción.

El administrador de sesiones incluido usa memoria local. Al reiniciar el proceso se pierden las sesiones y no se comparte el estado entre servidores. Antes de desplegar debe sustituirse por un almacén persistente y compartido. También falta implementar el controlador HTTP, HTTPS, las cookies, la protección CSRF según el diseño final, el control de intentos, el restablecimiento de contraseñas, los registros de auditoría y las pruebas de integración.

La tecnología de producción sigue pendiente en la documentación general. Por tanto, no se declara que el proyecto use actualmente JWT, OAuth, una base de datos específica ni un framework particular.

## Impacto esperado

- **Mantenibilidad:** la lógica de autenticación queda separada de la coordinación del inicio de sesión.
- **Flexibilidad:** se puede añadir una nueva estrategia respetando el mismo contrato.
- **Reutilización:** el servicio puede trabajar con distintas estrategias y repositorios.
- **Seguridad:** se evita devolver hashes y sales; el token se genera aleatoriamente y no se guarda en texto plano en el almacén del ejemplo.
- **Evolución:** el módulo puede convertirse más adelante en un servicio del backend cuando se decida la tecnología definitiva.

El patrón añade una interfaz y una clase concreta, por lo que introduce algo más de estructura que una función única. En este caso se justifica porque la autenticación es una parte central y es razonable prever más de un método de acceso.

## Cómo ejecutar las pruebas

Desde esta carpeta, con Python 3.10 o superior:

```bash
python -m unittest -v
```

Las pruebas usan un repositorio simulado. No requieren una base de datos ni servicios externos.

## Archivos de esta intervención

- `autenticacion_estrategia.py`: implementación de referencia.
- `test_autenticacion_estrategia.py`: pruebas unitarias.
- `diagrama-secuencia-autenticacion.puml`: diagrama de la solución.
- `README.md`: descripción y alcance.

## Fuentes técnicas

- OWASP, Password Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- OWASP, Session Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html
- Repositorio Educación Virtual RD, arquitectura inicial: https://github.com/Jeury2599/Educaci-n-Virtual-RD/blob/main/arquitectura/arquitectura.md
- Repositorio Educación Virtual RD, diagrama inicial de secuencia: https://github.com/Jeury2599/Educaci-n-Virtual-RD/blob/main/diagramas-uml/diagrama-de-secuencia.puml
