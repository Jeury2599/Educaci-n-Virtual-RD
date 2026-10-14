# Requisitos del sistema

## Alcance

Estos requisitos describen el comportamiento previsto de Educación Virtual RD. Se utilizan como base para el diseño; su cumplimiento deberá verificarse una vez desarrollada la plataforma.

## Requisitos funcionales

| Código | Requisito | Criterio de aceptación |
|---|---|---|
| RF01 | Registrar estudiantes con los datos básicos requeridos. | Si los campos obligatorios y el correo tienen un formato válido, el sistema permite enviar el registro; si hay errores, muestra qué debe corregirse. |
| RF02 | Permitir que un usuario inicie sesión. | Solo se concede el acceso con credenciales válidas; ante datos incorrectos, se muestra un mensaje claro sin revelar información sensible. |
| RF03 | Mostrar los cursos disponibles de manera organizada. | El estudiante puede consultar el catálogo y abrir la información de un curso disponible. |
| RF04 | Permitir realizar evaluaciones en línea. | El estudiante puede responder una evaluación y, al finalizar, consultar el resultado cuando corresponda a las reglas definidas. |
| RF05 | Mostrar el progreso académico. | El estudiante puede consultar un reporte asociado a sus cursos y evaluaciones, con datos coherentes con los registros disponibles. |
| RF06 | Facilitar la comunicación académica mediante un foro. | Si el foro se incluye en una versión futura, los usuarios autorizados pueden consultar y publicar mensajes conforme a las reglas que se definan. |

RF06 se considera una función complementaria propuesta; no forma parte de los cinco requisitos funcionales principales.

## Requisitos no funcionales

| Código | Requisito | Forma de verificación propuesta |
|---|---|---|
| RNF01 | Seguridad de acceso. | Probar contraseñas incorrectas, permisos de cada perfil y protección de rutas privadas. |
| RNF02 | Protección de información personal. | Revisar que cada usuario solo pueda consultar datos autorizados y que las contraseñas no se almacenen en texto plano. |
| RNF03 | Usabilidad. | Comprobar que los formularios tengan etiquetas claras, mensajes entendibles y navegación consistente. |
| RNF04 | Mantenibilidad. | Revisar la separación de responsabilidades y la organización del código por componentes. |
| RNF05 | Integridad de datos. | Verificar que inscripciones, resultados y reportes correspondan a registros válidos. |
| RNF06 | Compatibilidad. | Probar las pantallas principales en navegadores actuales y en tamaños de pantalla habituales. |

## Restricciones y supuestos

- El proyecto se encuentra en etapa de documentación y modelado.
- La tecnología de implementación todavía debe seleccionarse.
- Los criterios deben revisarse y ajustarse antes de dar por terminadas las pruebas.
- No se considera cumplido un requisito hasta que exista una implementación verificable o una evidencia documental cuando el trabajo sea exclusivamente de análisis.
