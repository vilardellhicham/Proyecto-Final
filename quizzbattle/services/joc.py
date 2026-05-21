from models.usuari import Usuari
from database.database import obtenir_nombreCuestionarios,conn

def jugar_questionari(usuari: Usuari): #questionari individual
    print("\n--- JUGAR QÜESTIONARI INDIVIDUAL ---")
    noms_questionaris=obtenir_nombreCuestionarios(conn)
    noms=[]
    for i in noms_questionaris:
        noms.append(i)

    print("Questionaris:")
    for i in range(len(noms)):
        print(f"{i+1}. {noms[i]}")

    num_q=int(input("Introdueix el numero de questionari: "))

    questionari_seleccionat=noms[num_q-1]





def mode_1vs1():
    print("\n--- MODE 1 VS 1 ---")