# Historias de usuario

Las historias describen necesidades desde el punto de vista de quien utilizaría la plataforma. Se presentan como base para el diseño y las pruebas futuras.

## HU01. Registro de estudiante

**Historia:** Como estudiante, quiero crear una cuenta con mis datos básicos para poder entrar a la plataforma.

**Criterios de aceptación:**
- El formulario solicita los datos obligatorios.
- El sistema valida que los datos tengan un formato correcto.
- Si hay campos incorrectos, indica qué debe corregirse.
- El registro no se confirma cuando faltan datos obligatorios.

**Requisito relacionado:** RF01.

## HU02. Inicio de sesión

**Historia:** Como usuario registrado, quiero iniciar sesión con mis credenciales para acceder a las funciones que me corresponden.

**Criterios de aceptación:**
- Se solicita correo y contraseña.
- Las credenciales se validan antes de conceder acceso.
- Los datos incorrectos producen un mensaje comprensible.
- Las secciones privadas no se muestran a usuarios sin autorización.

**Requisito relacionado:** RF02.

## HU03. Consulta de cursos

**Historia:** Como estudiante, quiero ver los cursos disponibles y su información para saber cuáles puedo tomar.

**Criterios de aceptación:**
- Se muestra una lista de cursos disponibles.
- Cada curso presenta, como mínimo, nombre y descripción.
- La información se presenta de forma legible.
- Si no hay cursos, se informa que el catálogo está vacío.

**Requisito relacionado:** RF03.

## HU04. Evaluaciones en línea

**Historia:** Como estudiante, quiero responder una evaluación en la plataforma para revisar lo que he aprendido.

**Criterios de aceptación:**
- La evaluación muestra las preguntas y las opciones disponibles.
- El sistema permite enviar las respuestas conforme a las reglas definidas.
- Al finalizar, muestra el resultado si la evaluación está configurada para corregirse automáticamente.
- Se evita enviar dos veces la misma respuesta de forma accidental, según las reglas que se implementen.

**Requisito relacionado:** RF04.

## HU05. Consulta de progreso

**Historia:** Como estudiante, quiero revisar mi progreso para conocer mis resultados y las actividades que he completado.

**Criterios de aceptación:**
- El reporte se relaciona con la cuenta autenticada.
- La información coincide con las evaluaciones e inscripciones registradas.
- Si todavía no existen resultados, el sistema lo comunica claramente.

**Requisito relacionado:** RF05.

## HU06. Participación en el foro

**Historia:** Como estudiante, quiero consultar y publicar mensajes en un foro para plantear dudas sobre mis cursos.

**Criterios de aceptación propuestos:**
- Los usuarios autorizados pueden consultar los temas.
- La plataforma identifica al autor de cada publicación.
- Se definen reglas para moderar y retirar contenido inapropiado.

**Requisito relacionado:** función complementaria RF06.
