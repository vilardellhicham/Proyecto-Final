from getpass import getpass

from services.autenticacio import registrar_usuario, iniciar_sesion


def registre_usuari():
    print("\n--- REGISTRE USUARI ---")
    nombre = input("Nom complet: ")
    nombre_usuario = input("Nom d'usuari: ")
    email = input("Email: ")
    contrasena = getpass("Contrasenya: ")
    confirmar_contrasena = getpass("Repeteix la contrasenya: ")

    if contrasena != confirmar_contrasena:
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
        print("Sessió iniciada correctament. Benvingut/da,", usuari_login["nombre_usuario"])
        return usuari_login
    else:
        print("Error: usuari/email o contrasenya incorrectes")
        return None


def importar_questionari():
    print("\n--- IMPORTAR QÜESTIONARI ---")
    print("Aquí anirà la importació del JSON")


def jugar_questionari():
    print("\n--- JUGAR QÜESTIONARI INDIVIDUAL ---")
    print("Aquí anirà la partida individual")


def mode_1vs1():
    print("\n--- MODE 1 VS 1 ---")
    print("Aquí anirà el mode competitiu")


def estadistiques_personals():
    print("\n--- ESTADÍSTIQUES PERSONALS ---")
    print("Aquí es mostraran les estadístiques de l'usuari")


def estadistiques_questionari():
    print("\n--- ESTADÍSTIQUES QÜESTIONARI ---")
    print("Aquí es mostraran les estadístiques del qüestionari")


def ranking_global():
    print("\n--- RÀNQUING GLOBAL ---")
    print("Aquí es mostrarà el rànquing global")


def menu_usuari(usuari_actual):
    opcio = ""

    while opcio != "8":
        print("\n===== MENÚ USUARI =====")
        print("Usuari connectat:", usuari_actual["nombre_usuario"])
        print("1. Importar qüestionari")
        print("2. Jugar qüestionari individual")
        print("3. Mode 1 vs 1")
        print("4. Consultar estadístiques personals")
        print("5. Consultar estadístiques qüestionari")
        print("6. Consultar rànquing global")
        print("7. Sortir")

        opcio = input("Escull una opció: ")

        match opcio:
            case "1":
                importar_questionari()
            case "2":
                jugar_questionari()
            case "3":
                mode_1vs1()
            case "4":
                estadistiques_personals()
            case "5":
                estadistiques_questionari()
            case "6":
                ranking_global()
            case "7":
                print("Tancant sessió...")
                opcio = "8"
            case _:
                print("Opció incorrecta")


def menu_principal():
    opcio = ""

    while opcio != "3":
        print("\n===== QUIZZBATTLE =====")
        print("1. Registre usuari")
        print("2. Iniciar sessió")
        print("3. Sortir")

        opcio = input("Escull una opció: ")

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