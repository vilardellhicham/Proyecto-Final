import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="quizzbattle",
    auth_plugin='mysql_native_password'
)

# ── USUARIS ──────────────────────────────────────────────────────────────────

def afegir_usuari(conn, nombre, nombre_usuario, contrasena, email):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (nombre, nombre_usuario, contrasena, email) VALUES (%s, %s, %s, %s)",
            (nombre, nombre_usuario, contrasena, email)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()

def obtenir_usuari(conn, id_usuario):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        return cursor.fetchone()
    finally:
        cursor.close()

def actualitzar_usuari(conn, id_usuario, nombre, nombre_usuario, contrasena, email):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE usuarios SET nombre=%s, nombre_usuario=%s, contrasena=%s, email=%s WHERE id_usuario=%s",
            (nombre, nombre_usuario, contrasena, email, id_usuario)
        )
        conn.commit()
        return cursor.rowcount == 1
    finally:
        cursor.close()

def actualitzar_estadistiques_usuari(conn, id_usuario, victoria, derrota, empat, puntuacio):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """UPDATE usuarios
               SET num_partidas = num_partidas + 1,
                   victorias    = victorias + %s,
                   derrotas     = derrotas  + %s,
                   empates      = empates   + %s,
                   puntuacion_total = puntuacion_total + %s
               WHERE id_usuario = %s""",
            (1 if victoria else 0, 1 if derrota else 0, 1 if empat else 0, puntuacio, id_usuario)
        )
        conn.commit()
    finally:
        cursor.close()

# ── CUESTIONARIS ─────────────────────────────────────────────────────────────

def afegir_cuestionario(conn, id_propietario, titulo, categoria, dificultad, descripcion):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO cuestionarios (id_propietario, titulo, categoria, dificultad, descripcion) VALUES (%s,%s,%s,%s,%s)",
            (id_propietario, titulo, categoria, dificultad, descripcion)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()

def obtenir_cuestionario(conn, id_cuestionario):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM cuestionarios WHERE id_cuestionario = %s", (id_cuestionario,))
        return cursor.fetchone()
    finally:
        cursor.close()

def obtenir_tots_cuestionaris(conn):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM cuestionarios ORDER BY titulo")
        return cursor.fetchall()
    finally:
        cursor.close()

def obtenir_cuestionari_per_titol_i_propietari(conn, titulo, id_propietario):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM cuestionarios WHERE titulo = %s AND id_propietario = %s",
            (titulo, id_propietario)
        )
        return cursor.fetchone()
    finally:
        cursor.close()

def actualitzar_cuestionario(conn, id_cuestionario, id_propietario, titulo, categoria, dificultad, descripcion):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE cuestionarios SET id_propietario=%s, titulo=%s, categoria=%s, dificultad=%s, descripcion=%s WHERE id_cuestionario=%s",
            (id_propietario, titulo, categoria, dificultad, descripcion, id_cuestionario)
        )
        conn.commit()
        return cursor.rowcount == 1
    finally:
        cursor.close()

# ── PREGUNTES ─────────────────────────────────────────────────────────────────

def afegir_pregunta(conn, id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """INSERT INTO preguntas
               (id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()

def obtenir_pregunta(conn, id_pregunta):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM preguntas WHERE id_pregunta = %s", (id_pregunta,))
        return cursor.fetchone()
    finally:
        cursor.close()

def obtenir_preguntes_per_cuestionari(conn, id_cuestionario):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT id_pregunta, id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos FROM preguntas WHERE id_cuestionario = %s",
            (id_cuestionario,)
        )
        return cursor.fetchall()
    finally:
        cursor.close()

def obtenir_nombrePreguntas(conn, id_cuestionario):
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM preguntas WHERE id_cuestionario = %s", (id_cuestionario,))
        count = cursor.fetchone()
        return count[0] if count else 0
    finally:
        cursor.close()

def actualitzar_pregunta(conn, id_pregunta, id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos):
    cursor = conn.cursor()
    try:
        cursor.execute(
            """UPDATE preguntas
               SET id_cuestionario=%s, tipo=%s, enunciado=%s, respuesta1=%s, respuesta2=%s,
                   respuesta3=%s, respuesta4=%s, respuesta_correcta=%s, puntos=%s
               WHERE id_pregunta=%s""",
            (id_cuestionario, tipo, enunciado, respuesta1, respuesta2, respuesta3, respuesta4, respuesta_correcta, puntos, id_pregunta)
        )
        conn.commit()
        return cursor.rowcount == 1
    finally:
        cursor.close()

def eliminar_preguntes_cuestionari(conn, id_cuestionario):
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM preguntas WHERE id_cuestionario = %s", (id_cuestionario,))
        conn.commit()
    finally:
        cursor.close()

# ── PARTIDES ──────────────────────────────────────────────────────────────────

def crear_partida(conn, id_cuestionario, tipo):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO partidas (id_cuestionario, tipo) VALUES (%s, %s)",
            (id_cuestionario, tipo)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()

def obtenir_partida(conn, id_partida):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM partidas WHERE id_partida = %s", (id_partida,))
        return cursor.fetchone()
    finally:
        cursor.close()

# ── RESULTATS ─────────────────────────────────────────────────────────────────

def crear_resultado(conn, id_partida, id_usuario, puntuacion, resultado):
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO resultados (id_partida, id_usuario, puntuacion, resultado) VALUES (%s,%s,%s,%s)",
            (id_partida, id_usuario, puntuacion, resultado)
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()

def obtenir_resultats(conn, id_partida):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM resultados WHERE id_partida = %s", (id_partida,))
        return cursor.fetchall()
    finally:
        cursor.close()

# ── ESTADÍSTIQUES ─────────────────────────────────────────────────────────────

def obtenir_estadistiques_usuari(conn, id_usuario):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT num_partidas, puntuacion_total, victorias FROM usuarios WHERE id_usuario = %s",
            (id_usuario,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()

def obtenir_estadistiques_cuestionari(conn, id_cuestionario):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """SELECT COUNT(r.id_resultado) AS vegades_jugat,
                      AVG(r.puntuacion)    AS puntuacio_mitjana,
                      MAX(r.puntuacion)    AS millor_puntuacio
               FROM partidas p
               JOIN resultados r ON p.id_partida = r.id_partida
               WHERE p.id_cuestionario = %s""",
            (id_cuestionario,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()

def obtenir_ranking_puntuacions(conn):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT nombre_usuario, puntuacion_total FROM usuarios ORDER BY puntuacion_total DESC LIMIT 10"
        )
        return cursor.fetchall()
    finally:
        cursor.close()

def obtenir_ranking_victories(conn):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT nombre_usuario, victorias FROM usuarios ORDER BY victorias DESC LIMIT 10"
        )
        return cursor.fetchall()
    finally:
        cursor.close()

def obtenir_ranking_partides(conn):
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT nombre_usuario, num_partidas FROM usuarios ORDER BY num_partidas DESC LIMIT 10"
        )
        return cursor.fetchall()
    finally:
        cursor.close()
