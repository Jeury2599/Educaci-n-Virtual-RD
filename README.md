Educación virtual R.D.
Descripción del Sistema
Educación Virtual RD es un sistema digital que tiene como objetivo hacer más fácil el acceso a los cursos virtuales para los estudiantes de la República Dominicana. La plataforma permite registrar usuarios, hacer login, consultar los cursos organizados, realizar evaluaciones en línea y visualizar reportes del progreso académico.

Objetivo
Crear una plataforma educativa que organice el proceso de aprendizaje virtual, facilitando el acceso a cursos, evaluaciones y reportes de rendimiento académico.

Problema que atiende
El sistema intenta satisfacer la necesidad de disponer de una plataforma educativa ordenada, accesible y segura. La solución permite tener centralizados los cursos, las evaluaciones, y el seguimiento del progreso académico de los estudiantes.

Principales funciones
Ficha de los alumnos.
Acceso seguro.
Gestión y consulta de cursos.
Realización de evaluaciones por Internet.
Ver los informes de progreso.
Arquitectura elegida
El sistema está organizado en una arquitectura cliente-servidor, con frontend, backend y base de datos. Esta arquitectura permite separar la interfaz que emplea el estudiante de la lógica que procesa la información y guarda los datos.

Organización del front-end y del back-end
Frente
La interfaz de usuario es la parte del sistema que el usuario ve y con la cual interactúa. Es responsable de mostrar formularios, cursos, evaluaciones, resultados y reportes de progreso. Recoge también las acciones del usuario y envía las peticiones al backend.

Parte posterior
El backend contiene la lógica principal del sistema. Su responsabilidad consiste en validar los datos, gestionar los usuarios, procesar las matriculas, administrar los cursos, corregir las evaluaciones y generar los informes académicos.

Database.
La base de datos guarda la información de usuarios, cursos, inscripciones, evaluaciones, calificaciones y reportes de progreso.

Mensaje del sistema
El frontend hace llamadas a una API para enviar solicitudes al backend. El backend recibe una petición, consulta o actualiza la base de datos y envía una respuesta al frontend. La interfaz muestra el resultado correspondiente para el usuario.

Flujo general :

Usuario → Frontend → API → Backend → BBDD

Base de datos > Backend > API > Frontend > Usuario

Herramientas usadas
GitHub para almacenar y controlar las evidencias.
GitHub Issues para dar de alta requerimientos, tareas y mejoras.
GitHub Projects para llevar la gestión del avance del proyecto.
Visual Paradigm Online para la elaboración de los diagramas UML.
Microsoft Word: para poner en orden los papeles.
PDF para entregar el producto final.
Principales requisitos funcionales
RF01. El sistema debe permitir registrar estudiantes.
RF02: El sistema debe permitir realizar un login seguro.
RF03: El sistema debe mostrar los cursos ordenados.
RF04. El sistema deberá permitir hacer evaluaciones en línea.
RF05. El sistema deberá generar reportes de progreso académico.
UML Diagrams
El proyecto contiene los siguientes modelos:

Diagrama de caso de uso.
Clase Diagram.
Diagrama de secuencia.
Esquema de actividades.
Los diagramas están guardados en la carpeta diagramas-uml.

Bitácora de cambios
Se identificaron cinco requisitos funcionales principales.
Se desarrollaron historias de usuario y criterios de aceptación.
Se hicieron los diagramas UML del sistema.
Se estableció la arquitectura cliente servidor.
Se han organizado los Issues y el tablero de GitHub Projects.
Situación actual del proyecto
El proyecto está en una versión inicial de documentación y modelado. Los requisitos principales, las historias de usuario, los diagramas UML y la arquitectura están definidos. Se deja para una próxima etapa la implementación del frontend, el backend y la base de datos.

Última versión
Versión 1.0.0 correspondiente al cierre inicial de documentación técnica y modelado de sistema.

Autor
Jeury Javier Sanchez
Estudiante de Ingeniería de Software
