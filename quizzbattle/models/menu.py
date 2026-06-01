from getpass import getpass

from services.autenticacio import registrar_usuario, iniciar_sesion
from services.importacio_json import ImportacioJSON
from services.joc import jugar_questionari, mode_1vs1
from services.estadistiques import (
    mostrar_estadistiques_personals,
    mostrar_estadistiques_questionari,
    mostrar_ranking_global,
)
from database.database import conn


def registre_usuari():
    print("\n--- REGISTRE USUARI ---")
    nombre = input("Nom complet: ")
    nombre_usuario = input("Nom d'usuari: ")
    email = input("Email: ")
    contrasena = getpass("Contrasenya: ")
    confirmar = getpass("Repeteix la contrasenya: ")

    if contrasena != confirmar:
        print("Error: les contrasenyes no coincideixen")
        return False

    registrat, missatge = registrar_usuario(nombre, nombre_usuario, contrasena, email)
    print(missatge)
    return registrat


def iniciar_sessio():
    print("\n--- INICIAR SESSIÓ ---")
    usuari = input("Usuari o email: ")
    contrasenya = getpass("Contrasenya: ")

    usuari_login = iniciar_sesion(usuari, contrasenya)

    if usuari_login is not None:
        print(f"Sessió iniciada correctament. Benvingut/da, {usuari_login['nombre_usuario']}!")
        return usuari_login
    else:
        print("Error: usuari/email o contrasenya incorrectes")
        return None


def importar_questionari(usuari_actual):
    print("\n--- IMPORTAR QÜESTIONARI ---")
    nom_fitxer = input("Nom del fitxer JSON (p.ex. data/quiz_test1.json): ").strip()

    importer = ImportacioJSON()
    dades = importer.llegir_fitxer(nom_fitxer)
    if dades is None:
        return

    if not importer.validar_json(dades):
        print("El fitxer JSON conté errors. No s'ha importat res.")
        return

    importer.mostrar_resum(dades)
    confirmacio = input("\nVols importar aquests qüestionaris? (S/N): ").strip().upper()
    if confirmacio != "S":
        print("Importació cancel·lada.")
        return

    creats, actualitzats = importer.importar_a_bd(conn, dades, usuari_actual["id_usuario"])
    print(f"\nQüestionaris creats:     {creats}")
    print(f"Qüestionaris actualitzats: {actualitzats}")


def menu_usuari(usuari_actual):
    opcio = ""

    while opcio != "7":
        print(f"\n===== MENÚ USUARI ({usuari_actual['nombre_usuario']}) =====")
        print("1. Importar qüestionari")
        print("2. Jugar qüestionari individual")
        print("3. Mode 1 vs 1")
        print("4. Consultar estadístiques personals")
        print("5. Consultar estadístiques qüestionari")
        print("6. Consultar rànquing global")
        print("7. Sortir")

        opcio = input("Escull una opció: ").strip()

        match opcio:
            case "1":
                importar_questionari(usuari_actual)
            case "2":
                jugar_questionari(usuari_actual)
            case "3":
                mode_1vs1(usuari_actual)
            case "4":
                mostrar_estadistiques_personals(usuari_actual)
            case "5":
                mostrar_estadistiques_questionari()
            case "6":
                mostrar_ranking_global()
            case "7":
                print("Tancant sessió...")
            case _:
                print("Opció incorrecta")


def menu_principal():
    opcio = ""

    while opcio != "3":
        print("\n===== QUIZZBATTLE =====")
        print("1. Registre usuari")
        print("2. Iniciar sessió")
        print("3. Sortir")

        opcio = input("Escull una opció: ").strip()

        match opcio:
            case "1":
                registre_usuari()
            case "2":
                usuari_actual = iniciar_sessio()
                if usuari_actual is not None:
                    menu_usuari(usuari_actual)
            case "3":
                print("Sortint del programa...")
            case _:
                print("Opció incorrecta")


if __name__ == "__main__":
    menu_principal()
