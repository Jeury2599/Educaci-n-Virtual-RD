# Guía de organización del proyecto

Esta guía resume cómo se organizó Educación Virtual RD durante la fase de análisis y documentación.

## 1. Descripción inicial

Primero se definió el propósito del sistema: reunir en una misma plataforma el acceso a cursos virtuales, las evaluaciones y la consulta del progreso académico. A partir de esa idea se identificaron los perfiles principales: estudiantes, docentes y administradores.

## 2. Requisitos

Se organizaron cinco requisitos funcionales:

- RF01: registro de estudiantes.
- RF02: inicio de sesión.
- RF03: consulta y organización de cursos.
- RF04: evaluaciones en línea.
- RF05: reportes de progreso.

Para que no quedaran como simples títulos, cada requisito se acompañó de una historia de usuario o un criterio que permita comprobar su comportamiento esperado. Los detalles están en la carpeta requisitos.

## 3. Modelado UML

Se agregaron archivos fuente PlantUML para cuatro diagramas: casos de uso, clases, secuencia y actividades. Cada archivo se puede abrir con una herramienta compatible con PlantUML para revisar o exportar el diagrama. Si la asignatura requiere capturas específicas de Visual Paradigm Online, deben tomarse desde esa herramienta y añadirse como evidencias reales.

## 4. Arquitectura

Se seleccionó como propuesta una arquitectura cliente-servidor organizada en frontend, backend, API y base de datos. La separación permite describir por separado la interfaz, las reglas del sistema y la información que debe almacenarse. Esta selección es conceptual; no implica que los componentes estén desplegados.

## 5. Seguimiento con GitHub

Los requisitos y tareas se registraron como Issues. Las descripciones se revisaron para explicar el resultado de la fase documental y sus criterios. Los Issues se cerraron porque esa definición documental queda atendida. Si se comienza la programación, conviene abrir nuevas tareas específicas de implementación y pruebas, en vez de reutilizar como pendientes los Issues de documentación.

## 6. Historial de cambios

Cada modificación de archivos se guardó mediante commits. Los títulos de los commits describen qué se actualizó. El registro resumido está en registro-de-cambios.md.

## 7. Alcance de la versión

La versión documental 1.0.0 reúne análisis, requisitos, modelos y arquitectura. La implementación funcional, las pruebas de integración y el despliegue todavía no forman parte de esta versión.

## 8. Cómo continuar

1. Revisar los requisitos con el profesor o con los posibles usuarios.
2. Revisar los modelos UML y exportar las imágenes definitivas.
3. Definir la tecnología concreta del frontend, backend y base de datos.
4. Crear nuevas Issues para implementación, seguridad, pruebas y despliegue.
5. Desarrollar por partes y mover las tareas a Done solo cuando exista evidencia de que el trabajo se completó.
