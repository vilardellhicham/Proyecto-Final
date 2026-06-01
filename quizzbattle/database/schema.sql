CREATE DATABASE IF NOT EXISTS quizzbattle;
USE quizzbattle;

CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    fecha_registro DATE DEFAULT (CURDATE()),
    num_partidas INT DEFAULT 0,
    victorias INT DEFAULT 0,
    derrotas INT DEFAULT 0,
    empates INT DEFAULT 0,
    puntuacion_total DECIMAL(10,2) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS cuestionarios (
    id_cuestionario INT AUTO_INCREMENT PRIMARY KEY,
    id_propietario INT NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    categoria VARCHAR(100),
    dificultad INT CHECK (dificultad BETWEEN 1 AND 5),
    descripcion TEXT,
    FOREIGN KEY (id_propietario) REFERENCES usuarios(id_usuario)
);

CREATE TABLE IF NOT EXISTS preguntas (
    id_pregunta INT AUTO_INCREMENT PRIMARY KEY,
    id_cuestionario INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    enunciado TEXT NOT NULL,
    respuesta1 VARCHAR(500),
    respuesta2 VARCHAR(500),
    respuesta3 VARCHAR(500),
    respuesta4 VARCHAR(500),
    respuesta_correcta INT NOT NULL CHECK (respuesta_correcta BETWEEN 1 AND 4),
    puntos INT NOT NULL DEFAULT 1,
    FOREIGN KEY (id_cuestionario) REFERENCES cuestionarios(id_cuestionario)
);

CREATE TABLE IF NOT EXISTS partidas (
    id_partida INT AUTO_INCREMENT PRIMARY KEY,
    id_cuestionario INT NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    fecha DATE DEFAULT (CURDATE()),
    FOREIGN KEY (id_cuestionario) REFERENCES cuestionarios(id_cuestionario)
);

CREATE TABLE IF NOT EXISTS resultados (
    id_resultado INT AUTO_INCREMENT PRIMARY KEY,
    id_partida INT NOT NULL,
    id_usuario INT NOT NULL,
    puntuacion DECIMAL(5,2),
    resultado VARCHAR(10),
    FOREIGN KEY (id_partida) REFERENCES partidas(id_partida),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);
