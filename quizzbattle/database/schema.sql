DROP TABLE IF EXISTS preguntas;
DROP TABLE IF EXISTS cuestionarios;
DROP TABLE IF EXISTS usuarios;


CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    
    nombre VARCHAR(100) NOT NULL,
    
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    
    contrasena VARCHAR(255) NOT NULL,
    
    email VARCHAR(150) NOT NULL UNIQUE,
    
    fecha_registro DATE NOT NULL DEFAULT (CURRENT_DATE),
    
    num_partidas INT NOT NULL DEFAULT 0,
    
    victorias INT NOT NULL DEFAULT 0,
    
    derrotas INT NOT NULL DEFAULT 0,
    
    empates INT NOT NULL DEFAULT 0,
    
    puntuacion_total DECIMAL(10,2) NOT NULL DEFAULT 0.00
);


CREATE TABLE cuestionarios (
    id_cuestionario INT PRIMARY KEY AUTO_INCREMENT,
    
    id_propietario INT NOT NULL,
    
    titulo VARCHAR(150) NOT NULL,
    
    categoria VARCHAR(100) NOT NULL,
    
    dificultad INT NOT NULL,
    
    descripcion TEXT,
    
    CONSTRAINT fk_cuestionario_usuario
        FOREIGN KEY (id_propietario)
        REFERENCES usuarios(id_usuario)
        ON DELETE CASCADE,
    
    CONSTRAINT chk_dificultad
        CHECK (dificultad BETWEEN 1 AND 5)
);


CREATE TABLE preguntas (
    id_pregunta INT PRIMARY KEY AUTO_INCREMENT,
    
    id_cuestionario INT NOT NULL,
    
    tipo VARCHAR(50) NOT NULL,
    
    enunciado TEXT NOT NULL,
    
    respuesta1 VARCHAR(255),
    
    respuesta2 VARCHAR(255),
    
    respuesta3 VARCHAR(255),
    
    respuesta4 VARCHAR(255),
    
    respuesta_correcta INT NOT NULL,
    
    puntos INT NOT NULL DEFAULT 1,
    
    CONSTRAINT fk_pregunta_cuestionario
        FOREIGN KEY (id_cuestionario)
        REFERENCES cuestionarios(id_cuestionario)
        ON DELETE CASCADE,
    
    CONSTRAINT chk_respuesta_correcta
        CHECK (respuesta_correcta BETWEEN 1 AND 4),
    
    CONSTRAINT chk_puntos
        CHECK (puntos IN (1, 2)),
    
    CONSTRAINT chk_tipo_pregunta
        CHECK (
            tipo IN (
                'VERDADERO_FALSO',
                'RESPUESTA_MULTIPLE',
                'RESPUESTA_NUMERICA',
                'RESPUESTA_CORTA',
                'TIEMPO_LIMITE'
            )
        )
);



CREATE INDEX idx_usuario_nombre
ON usuarios(nombre_usuario);

CREATE INDEX idx_cuestionario_categoria
ON cuestionarios(categoria);

CREATE INDEX idx_pregunta_tipo
ON preguntas(tipo);

CREATE INDEX idx_pregunta_cuestionario
ON preguntas(id_cuestionario);