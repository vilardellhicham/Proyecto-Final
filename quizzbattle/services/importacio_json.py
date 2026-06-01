import json

from database.database import (
    afegir_cuestionario, afegir_pregunta,
    obtenir_cuestionari_per_titol_i_propietari,
    actualitzar_cuestionario, eliminar_preguntes_cuestionari
)


class ImportacioJSON:

    def llegir_fitxer(self, nom_fitxer):
        try:
            with open(nom_fitxer, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: no s'ha trobat el fitxer JSON")
            return None
        except json.JSONDecodeError:
            print("Error: el fitxer JSON no té un format correcte")
            return None
        except Exception:
            print("Error inesperat llegint el fitxer JSON")
            return None

    def validar_json(self, dades):
        if dades is None:
            return False
        if "questionaris" not in dades:
            print("Error: falta l'apartat questionaris")
            return False
        if len(dades["questionaris"]) == 0:
            print("Error: no hi ha cap questionari")
            return False
        for q in dades["questionaris"]:
            for camp in ["titol", "categoria", "dificultat", "descripcio", "preguntes"]:
                if camp not in q:
                    print(f"Error: falta el camp '{camp}' en un questionari")
                    return False
            if len(q["preguntes"]) == 0:
                print("Error: un questionari no té preguntes")
                return False
            for p in q["preguntes"]:
                if not self.validar_pregunta(p):
                    return False
        return True

    def validar_pregunta(self, pregunta):
        camps = ["tipus", "enunciat", "resposta1", "resposta2", "resposta3", "resposta4", "resposta_correcta", "punts"]
        for camp in camps:
            if camp not in pregunta:
                print(f"Error: falta el camp '{camp}' en una pregunta")
                return False
        if pregunta["tipus"] not in ("VF", "MULTIPLE"):
            print("Error: tipus de pregunta incorrecte (ha de ser VF o MULTIPLE)")
            return False
        rc = pregunta["resposta_correcta"]
        if rc < 1 or rc > 4:
            print("Error: la resposta correcta ha de ser entre 1 i 4")
            return False
        if not pregunta[f"resposta{rc}"]:
            print("Error: la resposta correcta no pot estar buida")
            return False
        if pregunta["punts"] <= 0:
            print("Error: els punts han de ser superiors a 0")
            return False
        return True

    def mostrar_resum(self, dades):
        print("\n--- RESUM DELS QÜESTIONARIS ---")
        for q in dades["questionaris"]:
            print(f"\n  Títol:     {q['titol']}")
            print(f"  Categoria: {q['categoria']}")
            print(f"  Dificultat:{q['dificultat']}")
            print(f"  Preguntes: {len(q['preguntes'])}")

    def importar_a_bd(self, conn, dades, id_propietari):
        creats = 0
        actualitzats = 0

        for q in dades["questionaris"]:
            existing = obtenir_cuestionari_per_titol_i_propietari(conn, q["titol"], id_propietari)

            if existing:
                print(f"\nEl qüestionari '{q['titol']}' ja existeix.")
                opcio = input("Actualitzar (A) o guardar amb nou títol (N)? ").strip().upper()
                if opcio == "N":
                    nou_titol = input("Nou títol: ").strip()
                    if not nou_titol:
                        print("Títol buit. S'omet aquest qüestionari.")
                        continue
                    q = dict(q)
                    q["titol"] = nou_titol
                    existing = None

            if existing:
                id_q = existing["id_cuestionario"]
                actualitzar_cuestionario(conn, id_q, id_propietari, q["titol"], q["categoria"], q["dificultat"], q["descripcio"])
                eliminar_preguntes_cuestionari(conn, id_q)
                for p in q["preguntes"]:
                    afegir_pregunta(conn, id_q, p["tipus"], p["enunciat"],
                                    p.get("resposta1", ""), p.get("resposta2", ""),
                                    p.get("resposta3", ""), p.get("resposta4", ""),
                                    p["resposta_correcta"], p["punts"])
                actualitzats += 1
            else:
                id_q = afegir_cuestionario(conn, id_propietari, q["titol"], q["categoria"], q["dificultat"], q["descripcio"])
                if id_q:
                    for p in q["preguntes"]:
                        afegir_pregunta(conn, id_q, p["tipus"], p["enunciat"],
                                        p.get("resposta1", ""), p.get("resposta2", ""),
                                        p.get("resposta3", ""), p.get("resposta4", ""),
                                        p["resposta_correcta"], p["punts"])
                    creats += 1

        return creats, actualitzats
