import mysql.connector
conn = mysql.connector.connect(
host="localhost",
port=3306,#port local
user="root", #nom usuari
password="", #contrassenya
database="quizzbattle", #nom de la db
auth_plugin='mysql_native_password'
)