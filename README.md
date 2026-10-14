# Educación Virtual RD

## Descripción del sistema

Educación Virtual RD es una propuesta de plataforma para organizar cursos virtuales dirigidos a estudiantes de la República Dominicana. La idea es que el estudiante pueda crear una cuenta, entrar a la plataforma, consultar sus cursos, realizar evaluaciones y revisar su progreso académico desde un mismo lugar.

Este repositorio reúne la documentación del proyecto realizada durante Ingeniería de Software I. Por el momento, el alcance que se presenta es de análisis, requisitos, modelado y diseño. No se declara que la plataforma esté programada ni funcionando en producción.

## Problema que atiende

Cuando los cursos, evaluaciones y resultados se manejan por separado, al estudiante le puede resultar difícil encontrar el material y dar seguimiento a su aprendizaje. Educación Virtual RD plantea reunir esas funciones en una plataforma con una organización clara.

## Objetivo

Definir y documentar una plataforma educativa que permita organizar el aprendizaje virtual, con funciones de acceso de usuarios, consulta de cursos, evaluaciones y seguimiento del progreso.

## Usuarios principales

- **Estudiantes:** crean una cuenta, consultan cursos, realizan evaluaciones y revisan su progreso.
- **Docentes:** organizan el contenido de los cursos y preparan evaluaciones.
- **Administradores:** mantienen la información general y apoyan la gestión de los usuarios y cursos.

Los permisos específicos de cada perfil deberán definirse y probarse durante la implementación.

## Funcionalidades contempladas

1. Registro de estudiantes.
2. Inicio de sesión y control de acceso.
3. Consulta y organización de cursos.
4. Evaluaciones en línea con consulta de resultados.
5. Reportes de progreso académico.
6. Como función complementaria propuesta, un foro para estudiantes y docentes.

## Enfoque de trabajo

El proyecto se organizó mediante una forma de trabajo visual basada en Kanban. Las tareas se registran como GitHub Issues y se distribuyen en el tablero según su estado: por hacer, en progreso y completadas. Esto permite ver qué falta y dar seguimiento al trabajo.

El cierre de los Issues actuales corresponde a la etapa de análisis y documentación. No significa que las funciones estén implementadas en código. El desarrollo y las pruebas de la plataforma quedan como una etapa posterior.

## Requisitos principales

| Código | Requisito |
|---|---|
| RF01 | El sistema permitirá registrar estudiantes y validar los datos de entrada. |
| RF02 | El sistema permitirá iniciar sesión con credenciales válidas. |
| RF03 | El sistema mostrará los cursos de forma organizada. |
| RF04 | El sistema permitirá realizar evaluaciones en línea y consultar los resultados. |
| RF05 | El sistema permitirá consultar reportes de progreso académico. |

Los requisitos no funcionales, las historias de usuario y los criterios de aceptación se explican en la carpeta [requisitos](./requisitos/).

## Arquitectura seleccionada

Se propone una arquitectura cliente-servidor con tres partes: frontend, backend y base de datos. Esta separación permite organizar la interfaz, las reglas del sistema y el almacenamiento de la información sin mezclar todas las responsabilidades.

- **Frontend:** presenta las pantallas, formularios, cursos, evaluaciones y reportes.
- **Backend:** valida las solicitudes, aplica las reglas del sistema y coordina las operaciones.
- **Base de datos:** almacena usuarios, cursos, inscripciones, evaluaciones, calificaciones y datos de progreso.
- **API:** define la comunicación entre el frontend y el backend.

Flujo general: usuario → frontend → API → backend → base de datos. La respuesta vuelve por el backend y la API hasta el frontend.

La propuesta está explicada con más detalle en [arquitectura/arquitectura.md](./arquitectura/arquitectura.md).

## Modelos UML

El repositorio incluye archivos fuente para cuatro modelos: casos de uso, clases, secuencia y actividades. Los archivos están en [diagramas-uml](./diagramas-uml/). Se utilizan para explicar el alcance, las entidades principales y algunos flujos del sistema. Son modelos de diseño y no demuestran que el software ya esté implementado.

## Organización del repositorio

- [documentacion](./documentacion/): guía de organización, registro de cambios y nota técnica de versión.
- [requisitos](./requisitos/): requisitos, historias de usuario y criterios de aceptación.
- [diagramas-uml](./diagramas-uml/): archivos fuente de los modelos UML.
- [arquitectura](./arquitectura/): componentes, responsabilidades y comunicación.
- [evidencias](./evidencias/): guía para organizar capturas y enlaces de verificación.

## Herramientas utilizadas

- **GitHub:** almacenamiento del proyecto, historial de cambios e Issues.
- **GitHub Projects:** seguimiento visual de las tareas.
- **PlantUML:** archivos fuente editables de los modelos UML incluidos en este repositorio.
- **Visual Paradigm Online:** herramienta prevista para revisar o reproducir los modelos y capturar las evidencias requeridas por la asignatura.
- **Microsoft Word y PDF:** preparación del informe técnico y del entregable académico.

## Registro breve de cambios

1. Se organizaron los requisitos funcionales principales RF01–RF05.
2. Se redactaron historias de usuario y criterios de aceptación para orientar la validación.
3. Se incorporaron fuentes de cuatro modelos UML para representar el sistema.
4. Se documentó la arquitectura cliente-servidor y la comunicación entre frontend, backend y base de datos.
5. Se revisaron las descripciones de los Issues y se cerraron las tareas correspondientes a la fase de análisis y documentación.

El detalle de estos avances está en [documentacion/registro-de-cambios.md](./documentacion/registro-de-cambios.md). El listado de tareas y el alcance de sus cierres está en [documentacion/seguimiento-issues.md](./documentacion/seguimiento-issues.md).

## Estado actual

La documentación inicial y el modelado están organizados en el repositorio. Los Issues se cerraron para reflejar que su definición documental quedó atendida. Todavía queda pendiente implementar el frontend, el backend y la base de datos, además de probar las funciones con casos reales. Por eso, el proyecto no se presenta como una plataforma operativa.

## Versión documental

**Versión 1.0.0 — Documentación y modelado inicial.**

Esta versión agrupa la descripción del sistema, los requisitos, los modelos UML de referencia, la arquitectura y la gestión documental. La nota técnica está en [documentacion/nota-tecnica-version-1.0.0.md](./documentacion/nota-tecnica-version-1.0.0.md).

## Autor

**Jeury Javier Sánchez**  
Estudiante de Ingeniería de Software

---

Este repositorio presenta el estado de análisis y diseño del proyecto. Las funcionalidades descritas se consideran alcance previsto hasta que se implementen y se verifiquen mediante pruebas.
