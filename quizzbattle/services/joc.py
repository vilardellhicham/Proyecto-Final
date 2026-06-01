from getpass import getpass

from database.database import (
    conn,
    obtenir_tots_cuestionaris,
    obtenir_preguntes_per_cuestionari,
    crear_partida,
    crear_resultado,
    actualitzar_estadistiques_usuari,
)
from models.pregunta import crear_pregunta
from services.autenticacio import iniciar_sesion


def _seleccionar_cuestionari():
    cuestionaris = obtenir_tots_cuestionaris(conn)
    if not cuestionaris:
        print("No hi ha qüestionaris disponibles. Importa'n un primer.")
        return None

    print("\nQüestionaris disponibles:")
    for i, q in enumerate(cuestionaris, 1):
        print(f"  {i}. {q['titulo']}  [{q['categoria']}]  Dificultat: {q['dificultad']}")

    while True:
        try:
            num = int(input("\nSelecciona un qüestionari (0 per cancel·lar): "))
            if num == 0:
                return None
            if 1 <= num <= len(cuestionaris):
                return cuestionaris[num - 1]
        except ValueError:
            pass
        print("Opció invàlida.")


def _jugar_preguntes(preguntes, nom_jugador):
    encerts = 0
    errors = 0
    punts_obtinguts = 0
    punts_totals = sum(p.get_punts() for p in preguntes)

    print(f"\n=== Torn de {nom_jugador} ===")
    input("Prem ENTER per començar...")

    for i, pregunta in enumerate(preguntes, 1):
        print(f"\n[Pregunta {i}/{len(preguntes)}]")
        pregunta.mostrar()
        resposta = pregunta.demanar_resposta()

        if pregunta.validar_resposta(resposta):
            print("  Correcte!")
            encerts += 1
            punts_obtinguts += pregunta.get_punts()
        else:
            rc = pregunta.get_resposta_correcta()
            text_correcte = pregunta.get_respostes()[rc - 1]
            print(f"  Incorrecte. La resposta correcta era: {rc}. {text_correcte}")
            errors += 1

    return encerts, errors, punts_obtinguts, punts_totals


def jugar_questionari(usuari_actual):
    print("\n--- JUGAR QÜESTIONARI INDIVIDUAL ---")

    cuestionari = _seleccionar_cuestionari()
    if cuestionari is None:
        return

    dades_preguntes = obtenir_preguntes_per_cuestionari(conn, cuestionari["id_cuestionario"])
    if not dades_preguntes:
        print("Aquest qüestionari no té preguntes.")
        return

    preguntes = [crear_pregunta(d) for d in dades_preguntes]

    print(f"\n=== {cuestionari['titulo'].upper()} ===")
    print(f"Categoria: {cuestionari['categoria']}  |  Dificultat: {cuestionari['dificultad']}")
    if cuestionari.get("descripcion"):
        print(f"Descripció: {cuestionari['descripcion']}")

    encerts, errors, punts_obtinguts, punts_totals = _jugar_preguntes(preguntes, usuari_actual["nombre_usuario"])

    puntuacio_final = round((punts_obtinguts / punts_totals) * 10, 2) if punts_totals > 0 else 0.0

    print(f"\n{'='*30}")
    print(f"RESULTAT FINAL")
    print(f"  Encerts:    {encerts}")
    print(f"  Errors:     {errors}")
    print(f"  Puntuació:  {puntuacio_final:.2f} / 10")
    print(f"{'='*30}")

    id_partida = crear_partida(conn, cuestionari["id_cuestionario"], "INDIVIDUAL")
    if id_partida:
        crear_resultado(conn, id_partida, usuari_actual["id_usuario"], puntuacio_final, "WIN")
        actualitzar_estadistiques_usuari(conn, usuari_actual["id_usuario"], False, False, False, puntuacio_final)
        print("Resultat guardat a la base de dades.")


def mode_1vs1(usuari_actual):
    print("\n--- MODE 1 VS 1 ---")
    print(f"Jugador 1: {usuari_actual['nombre_usuario']}")

    print("\nIntrodueix les credencials del Jugador 2:")
    login2 = input("Usuari o email: ")
    passwd2 = getpass("Contrasenya: ")

    usuari2 = iniciar_sesion(login2, passwd2)
    if usuari2 is None:
        print("Credencials incorrectes. No es pot iniciar el mode 1 vs 1.")
        return
    if usuari2["id_usuario"] == usuari_actual["id_usuario"]:
        print("No pots jugar contra tu mateix.")
        return

    print(f"Jugador 2: {usuari2['nombre_usuario']}")

    cuestionari = _seleccionar_cuestionari()
    if cuestionari is None:
        return

    dades_preguntes = obtenir_preguntes_per_cuestionari(conn, cuestionari["id_cuestionario"])
    if not dades_preguntes:
        print("Aquest qüestionari no té preguntes.")
        return

    print(f"\n=== {cuestionari['titulo'].upper()} ===")
    print(f"Categoria: {cuestionari['categoria']}  |  Dificultat: {cuestionari['dificultad']}")

    preguntes1 = [crear_pregunta(d) for d in dades_preguntes]
    enc1, err1, pts1, punts_totals = _jugar_preguntes(preguntes1, usuari_actual["nombre_usuario"])
    punt1 = round((pts1 / punts_totals) * 10, 2) if punts_totals > 0 else 0.0

    preguntes2 = [crear_pregunta(d) for d in dades_preguntes]
    enc2, err2, pts2, _ = _jugar_preguntes(preguntes2, usuari2["nombre_usuario"])
    punt2 = round((pts2 / punts_totals) * 10, 2) if punts_totals > 0 else 0.0

    print(f"\n{'='*40}")
    print("RESULTATS FINALS")
    print(f"  {usuari_actual['nombre_usuario']:20s}  Encerts: {enc1}  Errors: {err1}  Puntuació: {punt1:.2f}/10")
    print(f"  {usuari2['nombre_usuario']:20s}  Encerts: {enc2}  Errors: {err2}  Puntuació: {punt2:.2f}/10")

    if punt1 > punt2:
        print(f"\n  Guanyador: {usuari_actual['nombre_usuario']}!")
        res1, res2 = "WIN", "LOSE"
        actualitzar_estadistiques_usuari(conn, usuari_actual["id_usuario"], True, False, False, punt1)
        actualitzar_estadistiques_usuari(conn, usuari2["id_usuario"], False, True, False, punt2)
    elif punt2 > punt1:
        print(f"\n  Guanyador: {usuari2['nombre_usuario']}!")
        res1, res2 = "LOSE", "WIN"
        actualitzar_estadistiques_usuari(conn, usuari_actual["id_usuario"], False, True, False, punt1)
        actualitzar_estadistiques_usuari(conn, usuari2["id_usuario"], True, False, False, punt2)
    else:
        print("\n  Empat!")
        res1, res2 = "DRAW", "DRAW"
        actualitzar_estadistiques_usuari(conn, usuari_actual["id_usuario"], False, False, True, punt1)
        actualitzar_estadistiques_usuari(conn, usuari2["id_usuario"], False, False, True, punt2)

    print(f"{'='*40}")

    id_partida = crear_partida(conn, cuestionari["id_cuestionario"], "VS")
    if id_partida:
        crear_resultado(conn, id_partida, usuari_actual["id_usuario"], punt1, res1)
        crear_resultado(conn, id_partida, usuari2["id_usuario"], punt2, res2)
        print("Resultats guardats a la base de dades.")
