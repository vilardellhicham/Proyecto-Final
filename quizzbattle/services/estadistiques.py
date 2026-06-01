from database.database import (
    conn,
    obtenir_tots_cuestionaris,
    obtenir_estadistiques_usuari,
    obtenir_estadistiques_cuestionari,
    obtenir_ranking_puntuacions,
    obtenir_ranking_victories,
    obtenir_ranking_partides,
)


def mostrar_estadistiques_personals(usuari_actual):
    print("\n--- ESTADÍSTIQUES PERSONALS ---")
    stats = obtenir_estadistiques_usuari(conn, usuari_actual["id_usuario"])
    if stats is None:
        print("No s'han pogut obtenir les estadístiques.")
        return

    num = stats["num_partidas"] or 0
    total = float(stats["puntuacion_total"] or 0)
    victories = stats["victorias"] or 0
    mitjana = round(total / num, 2) if num > 0 else 0.0

    print(f"  Qüestionaris realitzats: {num}")
    print(f"  Puntuació total:         {total:.2f}")
    print(f"  Puntuació mitjana:       {mitjana:.2f} / 10")
    print(f"  Victòries (1 vs 1):      {victories}")


def mostrar_estadistiques_questionari():
    print("\n--- ESTADÍSTIQUES QÜESTIONARI ---")
    cuestionaris = obtenir_tots_cuestionaris(conn)
    if not cuestionaris:
        print("No hi ha qüestionaris disponibles.")
        return

    print("\nQüestionaris disponibles:")
    for i, q in enumerate(cuestionaris, 1):
        print(f"  {i}. {q['titulo']}  [{q['categoria']}]")

    while True:
        try:
            num = int(input("\nSelecciona un qüestionari (0 per cancel·lar): "))
            if num == 0:
                return
            if 1 <= num <= len(cuestionaris):
                break
        except ValueError:
            pass
        print("Opció invàlida.")

    q = cuestionaris[num - 1]
    stats = obtenir_estadistiques_cuestionari(conn, q["id_cuestionario"])

    print(f"\n  Qüestionari: {q['titulo']}")
    if stats and stats["vegades_jugat"]:
        print(f"  Vegades jugat:      {stats['vegades_jugat']}")
        print(f"  Puntuació mitjana:  {float(stats['puntuacio_mitjana']):.2f} / 10")
        print(f"  Millor puntuació:   {float(stats['millor_puntuacio']):.2f} / 10")
    else:
        print("  Encara no s'ha jugat cap vegada.")


def mostrar_ranking_global():
    print("\n--- RÀNQUING GLOBAL ---")

    print("\n  TOP 10 PUNTUACIONS TOTALS:")
    print(f"  {'Pos':>3}  {'Usuari':<25}  {'Puntuació total':>15}")
    print("  " + "-" * 47)
    for i, r in enumerate(obtenir_ranking_puntuacions(conn), 1):
        print(f"  {i:>3}. {r['nombre_usuario']:<25}  {float(r['puntuacion_total']):>14.2f}")

    print("\n  USUARIS AMB MÉS VICTÒRIES:")
    print(f"  {'Pos':>3}  {'Usuari':<25}  {'Victòries':>10}")
    print("  " + "-" * 42)
    for i, r in enumerate(obtenir_ranking_victories(conn), 1):
        print(f"  {i:>3}. {r['nombre_usuario']:<25}  {r['victorias']:>10}")

    print("\n  USUARIS AMB MÉS QÜESTIONARIS COMPLETATS:")
    print(f"  {'Pos':>3}  {'Usuari':<25}  {'Partides':>9}")
    print("  " + "-" * 41)
    for i, r in enumerate(obtenir_ranking_partides(conn), 1):
        print(f"  {i:>3}. {r['nombre_usuario']:<25}  {r['num_partidas']:>9}")
