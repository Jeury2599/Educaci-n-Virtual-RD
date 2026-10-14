# Arquitectura propuesta

## Decisión

Para Educación Virtual RD se propone una arquitectura cliente-servidor separada en frontend, backend y base de datos. El frontend se comunica con el backend mediante una API. La selección es apropiada para el alcance inicial porque separa la experiencia del usuario de las reglas del negocio y el almacenamiento.

Esta es una decisión de diseño, no una descripción de componentes que ya estén desplegados.

## Componentes y responsabilidades

### Frontend

Es la parte con la que interactúan estudiantes, docentes y administradores. Incluye las pantallas de registro, acceso, catálogo de cursos, evaluaciones y reportes. También presenta mensajes cuando los datos no son válidos o cuando no hay información disponible.

### Backend

Recibe las solicitudes del frontend y aplica las reglas del sistema. Será responsable de validar datos, comprobar permisos, gestionar inscripciones, procesar evaluaciones y preparar los datos para los reportes.

### API

Define las operaciones que el frontend puede solicitar al backend y el formato de las respuestas. Deberá validar los datos de entrada y devolver errores con mensajes consistentes, evitando exponer información interna.

### Base de datos

Almacenará los usuarios, perfiles, cursos, inscripciones, evaluaciones, preguntas, intentos y resultados. Las relaciones deberán proteger la integridad de los datos y evitar registros huérfanos.

## Comunicación

1. El usuario realiza una acción en una pantalla.
2. El frontend envía una solicitud a la API.
3. El backend valida la solicitud y los permisos.
4. Si necesita datos, consulta o modifica la base de datos.
5. El backend devuelve el resultado a través de la API.
6. El frontend muestra la respuesta al usuario.

## Justificación

La separación reduce la mezcla de responsabilidades, facilita probar cada parte y permite cambiar la interfaz sin tener que rehacer toda la lógica. También hace más sencillo controlar los permisos y mantener la información en un único lugar.

## Seguridad que debe contemplarse

- Guardar contraseñas usando un algoritmo de hash adecuado, nunca en texto plano.
- Proteger las rutas privadas y comprobar los permisos en el backend.
- Validar datos tanto en la interfaz como en el servidor.
- Usar conexión cifrada cuando se despliegue el sistema.
- No incluir claves, contraseñas ni credenciales en el repositorio.
- Registrar errores técnicos sin guardar contraseñas u otros datos sensibles.

## Decisiones pendientes

Antes de implementar, se deben elegir el lenguaje y framework del frontend, la tecnología del backend, el motor de base de datos, el sistema de autenticación y el entorno de despliegue. Estas decisiones deben documentarse cuando se seleccionen y no presentarse como elegidas antes de tiempo.
