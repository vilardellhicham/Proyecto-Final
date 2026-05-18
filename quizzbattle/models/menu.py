from services.joc import jugar_questionari

def registre_usuari():
    print("\n--- REGISTRE USUARI ---")
    print("Aquí anirà el registre d'usuari")


def iniciar_sessio():
    print("\n--- INICIAR SESSIÓ ---")
    usuari = input("Usuari: ")
    contrasenya = input("Contrasenya: ")

    if usuari != "" and contrasenya != "":
        print("Sessió iniciada correctament")
        return True
    else:
        print("Error: usuari o contrasenya incorrectes")
        return False
    

def importar_questionari():
    print("\n--- IMPORTAR QÜESTIONARI ---")
    print("Aquí anirà la importació del JSON")



def estadistiques_personals():
    print("\n--- ESTADÍSTIQUES PERSONALS ---")
    print("Aquí es mostraran les estadístiques de l'usuari")


def estadistiques_questionari():
    print("\n--- ESTADÍSTIQUES QÜESTIONARI ---")
    print("Aquí es mostraran les estadístiques del qüestionari")


def ranking_global():
    print("\n--- RÀNQUING GLOBAL ---")
    print("Aquí es mostrarà el rànquing global")


def menu_usuari():
    opcio = ""

    while opcio != "8":
        print("\n===== MENÚ USUARI =====")
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
                #jugar_questionari(usuari, questionari)
                pass
            case "3":
                #mode_1vs1()
                pass
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
                login_correcte = iniciar_sessio()

                if login_correcte:
                    menu_usuari()
            case "3":
                print("Sortint del programa...")
            case _:
                print("Opció incorrecta")


if __name__ == "__main__":
    menu_principal()