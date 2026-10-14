Educación Virtual RD
Descripción del sistema
Educación Virtual RD es un sistema digital orientado a facilitar el acceso a cursos virtuales para estudiantes de la República Dominicana. La plataforma permite registrar usuarios, iniciar sesión, consultar cursos organizados, realizar evaluaciones en línea y visualizar reportes de progreso académico.

Objetivo
Desarrollar una plataforma educativa que permita organizar el proceso de aprendizaje virtual, facilitando el acceso a cursos, evaluaciones y reportes de rendimiento académico.

Problema que resuelve
El sistema busca responder a la necesidad de contar con una plataforma educativa organizada, accesible y segura. La solución permite centralizar los cursos, las evaluaciones y el seguimiento del progreso académico de los estudiantes.

Funcionalidades principales
Registro de estudiantes.
Inicio de sesión seguro.
Consulta y gestión de cursos.
Realización de evaluaciones en línea.
Visualización de reportes de progreso.
Arquitectura seleccionada
El sistema utiliza una arquitectura cliente-servidor organizada en frontend, backend y base de datos. Esta arquitectura permite separar la interfaz utilizada por el estudiante de la lógica encargada de procesar la información y almacenar los datos.

Organización del frontend y backend
Frontend
El frontend representa la parte visual del sistema con la que interactúa el usuario. Su responsabilidad es mostrar formularios, cursos, evaluaciones, resultados y reportes de progreso. También recoge las acciones realizadas por el usuario y envía las solicitudes al backend.

Backend
El backend contiene la lógica principal del sistema. Su responsabilidad es validar los datos, gestionar los usuarios, procesar las inscripciones, administrar los cursos, corregir las evaluaciones y generar los reportes académicos.

Base de datos
La base de datos almacena la información de usuarios, cursos, inscripciones, evaluaciones, calificaciones y reportes de progreso.

Comunicación del sistema
El frontend envía solicitudes al backend mediante una API. El backend procesa las solicitudes, consulta o actualiza la base de datos y devuelve una respuesta al frontend. La interfaz muestra el resultado correspondiente al usuario.

Flujo general:

Usuario → Frontend → API → Backend → Base de datos

Base de datos → Backend → API → Frontend → Usuario

Herramientas utilizadas
GitHub para el control y almacenamiento de las evidencias.
GitHub Issues para registrar requisitos, tareas y mejoras.
GitHub Projects para gestionar el avance del proyecto.
Visual Paradigm Online para elaborar los diagramas UML.
Microsoft Word para organizar la documentación.
PDF para presentar el entregable final.
Requisitos funcionales principales
RF01: El sistema debe permitir el registro de estudiantes.
RF02: El sistema debe permitir el inicio de sesión seguro.
RF03: El sistema debe mostrar los cursos organizados.
RF04: El sistema debe permitir realizar evaluaciones en línea.
RF05: El sistema debe generar reportes de progreso académico.
Modelos UML
El proyecto contiene los siguientes modelos:

Diagrama de casos de uso.
Diagrama de clases.
Diagrama de secuencia.
Diagrama de actividades.
Los diagramas se encuentran almacenados en la carpeta diagramas-uml.

Registro de cambios
Se documentaron cinco requisitos funcionales principales.
Se crearon historias de usuario y criterios de aceptación.
Se elaboraron los diagramas UML del sistema.
Se definió la arquitectura cliente-servidor.
Se organizaron los Issues y el tablero de GitHub Projects.
Estado actual del proyecto
El proyecto se encuentra en una versión inicial de documentación y modelado. Los requisitos principales, las historias de usuario, los diagramas UML y la arquitectura están definidos. La implementación del frontend, el backend y la base de datos queda pendiente para una próxima etapa.

Versión actual
Versión 1.0.0, correspondiente al cierre inicial de la documentación técnica y el modelado del sistema.

Autor
Jeury Javier Sánchez
Estudiante de Ingeniería de Software
