# Base de Datos Relacional
---------------------------------------------------------------------
Este proyecto consiste en el diseño y desarrollo de una base de datos relacional para la gestión de información sobre campus, promociones, estudiantes, profesores, clases, proyectos y modalidades. El diseño está basado en principios de normalización para garantizar la integridad y eficiencia en el manejo de los datos.
------------------------------------------------------------------------
---------------------------------------------------------------------------
## Tabla de Contenidos
-----------------------------------------------------------------
1. Descripción General
2. Diagrama Entidad-Relación
3.  Lógico
4. Estructura del Repositorio
----------------------------------------------------------------------------
## Descripción General
La base de datos está diseñada para soportar las operaciones necesarias en un entorno académico donde se gestionan las siguientes entidades:

* Campus: Ubicaciones físicas de la institución.
* Promociones: Cohortes de estudiantes asociadas a campus específicos.
* Clases: Cursos o asignaturas dentro de los campus.
* Estudiantes: Personas inscritas en promociones específicas.
* Profesores: Encargados de impartir clases y guiar a los estudiantes.
* Proyectos: Actividades académicas realizadas por los estudiantes.
* Modalidades: Tipos de enseñanza o aprendizaje en las clases.
* Notas: Evaluaciones de los estudiantes en proyectos.
* Verticales: Áreas temáticas asociadas a los proyectos.
-------------------------------------------------------------
--------------------------------------------------------------------
## Diagrama Entidad-Relación
-------------------------------------------------------------------
El diagrama E/R representa las entidades, atributos y las relaciones entre ellas. Este es el punto de partida del diseño lógico de la base de datos.
-----------------------------------------------------------------------
------------------------------------------------------------------------
Diagrama Entidad-Relación
--------------------------------------------------------------------------------
Modelo Lógico
A partir del modelo E/R, se desarrolló el modelo lógico, que incluye la estructura detallada de las tablas con sus claves primarias, foráneas y relaciones.
----------------------------------------------------------------------------------
-------------------------------------------------------------------------------------
Estructura del Proyecto
-------------------------------------------------------------------------------
Base_de_Datos_Relacional/ │ ├── diagramas/ │ ├── modelo_ER.png # Diagrama Entidad-Relación │ ├── modelo_logico.png # Diagrama del Modelo Lógico │ ├── scripts/ │ ├── crear_base_datos.sql # Scripts SQL para crear la base de datos │ ├── insertar_datos.sql # Scripts SQL para insertar datos de prueba │ ├── consultas.sql # Consultas SQL para explorar los datos │ ├── datos/ │ ├── estudiantes.csv # Datos iniciales de estudiantes │ ├── profesores.csv # Datos iniciales de profesores │ ├── proyectos.csv # Datos iniciales de proyectos │ └── README.md # Documentación del proyecto
