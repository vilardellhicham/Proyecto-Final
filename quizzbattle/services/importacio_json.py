import json


class ImportacioJSON:

    def llegir_fitxer(self, nom_fitxer):
        try:
            fitxer = open(nom_fitxer, "r", encoding="utf-8")
            dades = json.load(fitxer)
            fitxer.close()
            return dades

        except FileNotFoundError:
            print("Error: no s'ha trobat el fitxer JSON")
            return None

        except json.JSONDecodeError:
            print("Error: el fitxer JSON no te un format correcte")
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

        for questionari in dades["questionaris"]:

            if "titol" not in questionari:
                print("Error: falta el titol d'un questionari")
                return False

            if "categoria" not in questionari:
                print("Error: falta la categoria d'un questionari")
                return False

            if "dificultat" not in questionari:
                print("Error: falta la dificultat d'un questionari")
                return False

            if "descripcio" not in questionari:
                print("Error: falta la descripcio d'un questionari")
                return False

            if "preguntes" not in questionari:
                print("Error: falta la llista de preguntes")
                return False

            if len(questionari["preguntes"]) == 0:
                print("Error: un questionari no te preguntes")
                return False

            for pregunta in questionari["preguntes"]:
                if self.validar_pregunta(pregunta) == False:
                    return False

        return True


    def validar_pregunta(self, pregunta):
        camps = [
            "tipus",
            "enunciat",
            "resposta1",
            "resposta2",
            "resposta3",
            "resposta4",
            "resposta_correcta",
            "punts"
        ]

        for camp in camps:
            if camp not in pregunta:
                print("Error: falta el camp", camp, "en una pregunta")
                return False

        if pregunta["tipus"] != "VF" and pregunta["tipus"] != "MULTIPLE":
            print("Error: tipus de pregunta incorrecte")
            return False

        if pregunta["resposta_correcta"] < 1 or pregunta["resposta_correcta"] > 4:
            print("Error: la resposta correcta ha de ser entre 1 i 4")
            return False

        resposta_correcta = "resposta" + str(pregunta["resposta_correcta"])

        if pregunta[resposta_correcta] == "":
            print("Error: la resposta correcta no pot estar buida")
            return False

        if pregunta["punts"] <= 0:
            print("Error: els punts han de ser superiors a 0")
            return False

        return True


    def mostrar_resum(self, dades):
        print("\n--- RESUM DELS QUESTIONARIS ---")

        for questionari in dades["questionaris"]:
            print("\nTitol:", questionari["titol"])
            print("Categoria:", questionari["categoria"])
            print("Dificultat:", questionari["dificultat"])
            print("Nombre de preguntes:", len(questionari["preguntes"]))