import mysql.connector
conn = mysql.connector.connect(
host="localhost",
port=3306,#port local
user="root", #nom usuari
password="", #contrassenya
database="quizzbattle", #nom de la db
auth_plugin='mysql_native_password'
)

def afegir_usuari(conn, nombre_usuario, contrasena, email):
    cursor = conn.cursor()
    
    INSERT_QUERY = """
    INSERT INTO usuarios (nombre_usuario, contrasena, email)
    VALUES (%s, %s, %s)
    """
    valors = (nombre_usuario, contrasena, email)
    
    cursor.execute(INSERT_QUERY, valors) 
    
    conn.commit() 
    
    cursor.close() 
    
    num_files = cursor.rowcount
    
    if num_files == 1:
        return True
    else:
        return False

def obtenir_usuari(conn, id_usuari):
    cursor = conn.cursor()
    
    SELECT_QUERY = """
    SELECT * FROM usuaris WHERE id_usuaris = %s
    """
    valors = (id_usuari,)
    
    cursor.execute(SELECT_QUERY, valors)
    
    usuari = cursor.fetchone() 
    
    cursor.close()
    
    if usuari:
        return usuari
    else:
        return None
