#logica del log in

import hashlib
import mysql.connector

from database.database import conn


def _hash_contrasena(contrasena: str) -> str:
    return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()


def registrar_usuario(nombre: str, nombre_usuario: str, contrasena: str, email: str) -> tuple[bool, str]:
    if nombre.strip() == "" or nombre_usuario.strip() == "" or contrasena.strip() == "" or email.strip() == "":
        return False, "No puedes dejar campos vacíos."

    contrasena_cifrada = _hash_contrasena(contrasena)
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO usuarios (nombre, nombre_usuario, contrasena, email)
            VALUES (%s, %s, %s, %s)
            """,
            (nombre, nombre_usuario, contrasena_cifrada, email)
        )
        conn.commit()
        return True, "Usuario registrado correctamente."

    except mysql.connector.IntegrityError:
        return False, "El nombre de usuario o el email ya existen."

    except mysql.connector.Error as error:
        return False, f"Error de base de datos: {error}"

    finally:
        cursor.close()


def iniciar_sesion(usuario_o_email: str, contrasena: str):
    if usuario_o_email.strip() == "" or contrasena.strip() == "":
        return None

    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT id_usuario, nombre, nombre_usuario, contrasena, email,
                   fecha_registro, num_partidas, victorias, derrotas, empates, puntuacion_total
            FROM usuarios
            WHERE nombre_usuario = %s OR email = %s
            """,
            (usuario_o_email, usuario_o_email)
        )
        usuario = cursor.fetchone()

        if usuario is None:
            return None

        contrasena_cifrada = _hash_contrasena(contrasena)

        if usuario["contrasena"] == contrasena_cifrada:
            return usuario

        if usuario["contrasena"] == contrasena:
            return usuario

        return None

    except mysql.connector.Error as error:
        print("Error de base de datos:", error)
        return None

    finally:
        cursor.close()