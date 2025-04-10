-- Eliminar tablas si existen
DROP TABLE IF EXISTS campus CASCADE;
DROP TABLE IF EXISTS promocion CASCADE;
DROP TABLE IF EXISTS vertical CASCADE;
DROP TABLE IF EXISTS modalidad CASCADE;
DROP TABLE IF EXISTS grupo CASCADE;
DROP TABLE IF EXISTS profesores CASCADE;
DROP TABLE IF EXISTS alumnos CASCADE;
DROP TABLE IF EXISTS proyectos CASCADE;
DROP TABLE IF EXISTS calificaciones CASCADE;


-- Crear tabla campus
CREATE TABLE campus (
  id_campus serial NOT NULL PRIMARY KEY, 
  ciudad varchar(50) NOT NULL
);

-- Crear tabla promocion
CREATE TABLE promocion(
  id_promocion serial NOT NULL PRIMARY KEY, 
  mes varchar(50) NOT NULL
);

-- Crear tabla modalidad
CREATE TABLE modalidad(
  id_modalidad serial NOT NULL PRIMARY KEY, 
  modo varchar(50) NOT NULL
);

-- Crear tabla vertical
CREATE TABLE vertical(
  id_vertical serial NOT NULL PRIMARY KEY, 
  curso varchar(25) NOT NULL
);

-- Crear tabla grupo
CREATE TABLE grupo (
  id_grupo serial NOT NULL PRIMARY KEY, 
  id_promocion int,
  id_campus int,
  id_modalidad int,
  id_vertical int,
  FOREIGN KEY (id_promocion) REFERENCES promocion(id_promocion),
  FOREIGN KEY (id_campus) REFERENCES campus(id_campus),
  FOREIGN KEY (id_modalidad) REFERENCES modalidad(id_modalidad),
  FOREIGN KEY (id_vertical) REFERENCES vertical(id_vertical)
);
-- Crear tabla profesores
CREATE TABLE profesores (
  id_profesor serial PRIMARY KEY, 
  nombre varchar(45) NOT NULL,  
  email varchar(100) NOT NULL UNIQUE,
  rol varchar(25),
  id_grupo int,
  FOREIGN KEY (id_grupo) REFERENCES grupo(id_grupo)

);

-- Crear tabla alumnos
CREATE TABLE alumnos (
  id_alumno serial NOT NULL PRIMARY KEY,
  nombre varchar(50) NOT NULL,
  email varchar(100) NOT NULL UNIQUE,
  id_grupo int,
  FOREIGN KEY (id_grupo) REFERENCES grupo(id_grupo)
);

-- Crear tabla Proyecto
CREATE TABLE proyecto (
  id_proyecto serial NOT NULL PRIMARY KEY,
  nombre_proyecto varchar(50) NOT NULL
 );

-- Crear tabla calificaciones
CREATE TABLE calificaciones (
  id_calificaciones serial NOT NULL PRIMARY KEY,
  nota varchar(25),
  id_alumno int,
  id_proyecto int,
  FOREIGN KEY (id_proyecto) REFERENCES proyecto(id_proyecto),
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)
 );