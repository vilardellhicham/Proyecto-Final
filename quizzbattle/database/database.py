import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="quizzbattle",
    auth_plugin='mysql_native_password'
)

def afegir_usuari(conn, nombre, nombre_usuario, contrasena, email):
    cursor = conn.cursor()
    INSERT_QUERY = """
    INSERT INTO usuarios (nombre, nombre_usuario, contrasena, email)
    VALUES (%s, %s, %s, %s)
    """
    valors = (nombre, nombre_usuario, contrasena, email)
    cursor.execute(INSERT_QUERY, valors)
    conn.commit()
    cursor.close()
    return cursor.rowcount == 1

def obtenir_usuari(conn, id_usuario):
    cursor = conn.cursor()
    SELECT_QUERY = """
    SELECT * FROM usuarios WHERE id_usuario = %s
    """
    valors = (id_usuario,)
    cursor.execute(SELECT_QUERY, valors)
    usuario_data = cursor.fetchone()
    cursor.close()
    return usuario_data

def actualitzar_usuari(conn, id_usuario, nombre, nombre_usuario, contrasena, email):
    cursor = conn.cursor()
    UPDATE_QUERY = """
    UPDATE usuarios 
    SET nombre = %s, nombre_usuario = %s, contrasena = %s, email = %s 
    WHERE id_usuario = %s
    """
    valors = (nombre, nombre_usuario, contrasena, email, id_usuario)
    cursor.execute(UPDATE_QUERY, valors)
    conn.commit()
    cursor.close()
    return cursor.rowcount == 1

def afegir_cuestionario(conn, id_propietario, titulo, categoria, dificultad, descripcion):
    cursor = conn.cursor()
    INSERT_QUERY = """
    INSERT INTO cuestionarios (id_propietario, titulo, categoria, dificultad, descripcion)
    VALUES (%s, %s, %s, %s, %s)
    """
    valors = (id_propietario, titulo, categoria, dificultad, descripcion)
    cursor.execute(INSERT_QUERY, valors)
    conn.commit()
    cursor.close()
    return cursor.rowcount == 1

def obtenir_cuestionario(conn, id_cuestionario):
    cursor = conn.cursor()
    SELECT_QUERY = """
    SELECT * FROM cuestionarios WHERE id_cuestionario = %s
    """
    valors = (id_cuestionario,)
    cursor.execute(SELECT_QUERY, valors)
    cuestionario_data = cursor.fetchone()
    cursor.close()
    return cuestionario_data

def actualitzar_cuestionario(conn, id_cuestionario, id_propietario, titulo, categoria, dificultad, descripcion):
    cursor = conn.cursor()
    UPDATE_QUERY = """
    UPDATE cuestionarios 
    SET id_propietario = %s, titulo = %s, categoria = %s, dificultad = %s, descripcion = %s 
    WHERE id_cuestionario = %s
    """
    valors = (id_propietario, titulo, categoria, dificultad, descripcion, id_cuestionario)
    cursor.execute(UPDATE_QUERY, valors)
    conn.commit()
    cursor.close()
    return cursor.rowcount == 1

def obtenir_nombreCuestionarios(conn):
    cursor = conn.cursor()
    SELECT_QUERY = """
    SELECT COUNT(*) FROM cuestionarios
    """
    cursor.execute(SELECT_QUERY)
    count = cursor.fetchone()[0]
    cursor.close()
    return count

def afegir_pregunta(conn, id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos):
    cursor = conn.cursor()
    INSERT_QUERY = """
    INSERT INTO preguntas (id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valors = (id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos)
    cursor.execute(INSERT_QUERY, valors)
    conn.commit()
    cursor.close()
    return cursor.rowcount == 1

def obtenir_pregunta(conn, id_pregunta):
    cursor = conn.cursor()
    SELECT_QUERY = """
    SELECT * FROM preguntas WHERE id_pregunta = %s
    """
    valors = (id_pregunta,)
    cursor.execute(SELECT_QUERY, valors)
    pregunta_data = cursor.fetchone()
    cursor.close()
    return pregunta_data

def actualitzar_pregunta(conn, id_pregunta, id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos):
    cursor = conn.cursor()
    UPDATE_QUERY = """
    UPDATE preguntas 
    SET id_cuestionario = %s, tipo = %s, enunciado = %s, respuesta1 = %s, respuesta2 = %s, respuesta3 = %s, respuesta4 = %s, respuesta_correcta = %s, puntos = %s 
    WHERE id_pregunta = %s
    """
    valors = (id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos, id_pregunta)
    cursor.execute(UPDATE_QUERY, valors)
    conn.commit()
    cursor.close()
    return cursor.rowcount == 1
