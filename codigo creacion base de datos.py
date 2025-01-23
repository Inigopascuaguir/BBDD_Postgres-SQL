

-- Crear la tabla Campus
CREATE TABLE Campus (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Crear la tabla Promoción
CREATE TABLE Promoción (
    id SERIAL PRIMARY KEY,
    id_campus INT REFERENCES Campus(id),
    fecha_comienzo DATE NOT NULL
);

-- Crear la tabla Estudiante
CREATE TABLE Estudiante (
    id SERIAL PRIMARY KEY,
    id_promoción INT REFERENCES Promoción(id),
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Crear la tabla Notas
CREATE TABLE Notas (
    id SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES Estudiante(id),
    nombre_proyecto VARCHAR(255) NOT NULL,
    nota VARCHAR(255) NOT NULL
);

-- Crear la tabla Profesores
CREATE TABLE Profesores (
    id SERIAL PRIMARY KEY,
    id_promoción INT REFERENCES Promoción(id),
    rol VARCHAR(255) NOT NULL,
    nombre_profesor VARCHAR(255) NOT NULL
);

-- Crear la tabla Proyectos
CREATE TABLE Proyectos (
    id SERIAL PRIMARY KEY,
    nombre_proyecto VARCHAR(255) NOT NULL
);

-- Crear la tabla Aula
CREATE TABLE Aula (
    id SERIAL PRIMARY KEY,
    id_campus INT REFERENCES Campus(id),
    nombre_aula VARCHAR(255) NOT NULL
);

-- Crear la tabla Modalidad
CREATE TABLE Modalidad (
    id SERIAL PRIMARY KEY,
    nombre_modalidad VARCHAR(255) NOT NULL
);

-- Crear la tabla Proyectos_Vertical
CREATE TABLE Proyectos_Vertical (
    id_proyecto INT REFERENCES Proyectos(id),
    id_vertical INT,
    PRIMARY KEY (id_proyecto, id_vertical)
);

-- Crear la tabla Vertical
CREATE TABLE Vertical (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Insertar datos en la tabla Campus
INSERT INTO Campus (nombre) VALUES ('Madrid'), ('Valencia');

-- Insertar datos en la tabla Promoción
INSERT INTO Promoción (id_campus, fecha_comienzo) VALUES 
(1, '2023-09-18'), 
(1, '2024-02-12'), 
(2, '2024-02-12'),
(2, '2023-09-18');

-- Insertar datos en la tabla Estudiante
INSERT INTO Estudiante (id_promoción, nombre, email) VALUES 
(1, 'Jafet Casals', 'Jafet_Casals@gmail.com'),
(1, 'Jorge Manzanares', 'Jorge_Manzanares@gmail.com'),
(1, 'Onofre Adadia', 'Onofre_Adadia@gmail.com'),
(1, 'Merche Prada', 'Merche_Prada@gmail.com'),
(1, 'Pilar Abella', 'Pilar_Abella@gmail.com'),
(1, 'Leoncio Tena', 'Leoncio_Tena@gmail.com'),
(1, 'Odalys Torrijos', 'Odalys_Torrijos@gmail.com'),
(1, 'Eduardo Caparrós', 'Eduardo_Caparrós@gmail.com'),
(1, 'Ignacio Goicoechea', 'Ignacio_Goicoechea@gmail.com'),
(1, 'Clementina Santos', 'Clementina_Santos@gmail.com'),
(1, 'Daniela Falcó', 'Daniela_Falcó@gmail.com'),
(1, 'Abraham Vélez', 'Abraham_Vélez@gmail.com'),
(1, 'Maximiliano Menéndez', 'Maximiliano_Menéndez@gmail.com'),
(1, 'Anita Heredia', 'Anita_Heredia@gmail.com'),
(1, 'Eli Casas', 'Eli_Casas@gmail.com'),
(2, 'Guillermo Borrego', 'Guillermo_Borrego@gmail.com'),
(2, 'Sergio Aguirre', 'Sergio_Aguirre@gmail.com'),
(2, 'Carlito Carrión', 'Carlito_Carrión@gmail.com'),
(2, 'Haydée Figueroa', 'Haydée_Figueroa@gmail.com'),
(2, 'Chita Mancebo', 'Chita_Mancebo@gmail.com'),
(2, 'Joaquina Asensio', 'Joaquina_Asensio@gmail.com'),
(2, 'Cristian Sarabia', 'Cristian_Sarabia@gmail.com'),
(2, 'Isabel Ibáñez', 'Isabel_Ibáñez@gmail.com'),
(2, 'Desiderio Jordá', 'Desiderio_Jordá@gmail.com'),
(2, 'Rosalina Llanos', 'Rosalina_Llanos@gmail.com'),
(3, 'Amor Larrañaga', 'Amor_Larrañaga@gmail.com'),
(3, 'Teodoro Alberola', 'Teodoro_Alberola@gmail.com'),
(3, 'Cleto Plana', 'Cleto_Plana@gmail.com'),
(3, 'Aitana Sebastián', 'Aitana_Sebastián@gmail.com'),
(3, 'Dolores Valbuena', 'Dolores_Valbuena@gmail.com'),
(3, 'Julie Ferrer', 'Julie_Ferrer@gmail.com'),
(3, 'Mireia Cabañas', 'Mireia_Cabañas@gmail.com'),
(3, 'Flavia Amador', 'Flavia_Amador@gmail.com'),
(3, 'Albino Macias', 'Albino_Macias@gmail.com'),
(3, 'Ester Sánchez', 'Ester_Sánchez@gmail.com'),
(3, 'Luis Miguel Galvez', 'Luis_Miguel_Galvez@gmail.com'),
(3, 'Loida Arellano', 'Loida_Arellano@gmail.com'),
(3, 'Heraclio Duque', 'Heraclio_Duque@gmail.com'),
(3, 'Herberto Figueras', 'Herberto_Figueras@gmail.com'),
(4, 'Teresa Laguna', 'Teresa_Laguna@gmail.com'),
(4, 'Estrella Murillo', 'Estrella_Murillo@gmail.com'),
(4, 'Ernesto Uriarte', 'Ernesto_Uriarte@gmail.com'),
(4, 'Daniela Guitart', 'Daniela_Guitart@gmail.com'),
(4, 'Timoteo Trillo', 'Timoteo_Trillo@gmail.com'),
(4, 'Ricarda Tovar', 'Ricarda_Tovar@gmail.com'),
(4, 'Alejandra Vilaplana', 'Alejandra_Vilaplana@gmail.com'),
(4, 'Daniel Rosselló', 'Daniel_Rosselló@gmail.com'),
(4, 'Rita Olivares', 'Rita_Olivares@gmail.com'),
(4, 'Cleto Montes', 'Cleto_Montes@gmail.com'),
(4, 'Marino Castilla', 'Marino_Castilla@gmail.com'),
(4, 'Estefanía Valcárcel', 'Estefanía_Valcárcel@gmail.com'),
(4, 'Noemí Vilanova', 'Noemí_Vilanova@gmail.com');

-- Insertar datos en la tabla Profesores
INSERT INTO Profesores (id_promoción, rol, nombre_profesor) VALUES 
(1, 'TA', 'Noa Yáñez'),
(1, 'TA', 'Saturnina Benitez'),
(1, 'TA', 'Anna Feliu'),
(3, 'TA', 'Rosalva Ayuso'),
(4, 'TA', 'Ana Sofía Ferrer'),
(4, 'TA', 'Angélica Corral'),
(1, 'TA', 'Ariel Lledó'),
(4, 'LI', 'Mario Prats'),
(2, 'LI', 'Luis Ángel Suárez'),
(1, 'LI', 'María Dolores Diaz');

-- Insertar datos en la tabla Proyectos
INSERT INTO Proyectos (nombre_proyecto) VALUES 
('Proyecto_HLF'),
('Proyecto_EDA'),
('Proyecto_BBDD'),
('Proyecto_ML'),
('Proyecto_Deployment'),
('Proyecto_WebDev'),
('Proyecto_FrontEnd'),
('Proyecto_Backend'),
('Proyecto_React'),
('Proyecto_FullSatck');

-- Insertar datos en la tabla Notas
INSERT INTO Notas (id_estudiante, nombre_proyecto, nota) VALUES 
(1, 'Proyecto_HLF', 'Apto'),
(1, 'Proyecto_EDA', 'No Apto'),
(1, 'Proyecto_BBDD', 'Apto'),
(1, 'Proyecto_ML', 'Apto'),
(1, 'Proyecto_Deployment', 'Apto'),
(2, 'Proyecto_HLF', 'Apto'),
(2, 'Proyecto_EDA', 'No Apto'),
(2, 'Proyecto_BBDD', 'Apto'),
(2, 'Proyecto_ML', 'Apto'),
(2, 'Proyecto_Deployment', 'Apto'),
(3, 'Proyecto_HLF', 'Apto'),
(3, 'Proyecto_EDA', 'Apto'),
(3, 'Proyecto_BBDD', 'Apto'),
(3, 'Proyecto_ML', 'No Apto'),
(3, 'Proyecto_Deployment', 'Apto'),
(4, 'Proyecto_HLF', 'Apto'),
(4, 'Proyecto_EDA', 'No Apto'),
(4, 'Proyecto_BBDD', 'No Apto'),
(4, 'Proyecto_ML', 'Apto'),
(4, 'Proyecto_Deployment', 'No Apto')
