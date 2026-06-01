from abc import ABC, abstractmethod


class Pregunta(ABC):
    def __init__(self, id_pregunta, id_cuestionario, tipus, enunciat, respostes, resposta_correcta, punts):
        self._id_pregunta = id_pregunta
        self._id_cuestionario = id_cuestionario
        self._tipus = tipus
        self._enunciat = enunciat
        self._respostes = respostes  # list of 4 elements
        self._resposta_correcta = resposta_correcta
        self._punts = punts

    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def demanar_resposta(self):
        pass

    def validar_resposta(self, resposta_usuari):
        return int(resposta_usuari) == self._resposta_correcta

    # GETTERS
    def get_id_pregunta(self):
        return self._id_pregunta

    def get_tipus(self):
        return self._tipus

    def get_enunciat(self):
        return self._enunciat

    def get_respostes(self):
        return self._respostes

    def get_resposta_correcta(self):
        return self._resposta_correcta

    def get_punts(self):
        return self._punts

    # SETTERS
    def set_enunciat(self, valor):
        self._enunciat = valor

    def set_punts(self, valor):
        self._punts = valor


class PreguntaVF(Pregunta):
    def mostrar(self):
        print(f"\n{self._enunciat}")
        print("  1. Verdader")
        print("  2. Fals")

    def demanar_resposta(self):
        while True:
            try:
                r = int(input("Tria (1 o 2): "))
                if r in [1, 2]:
                    return r
            except ValueError:
                pass
            print("Resposta invàlida. Introdueix 1 o 2.")


class PreguntaMultiple(Pregunta):
    def mostrar(self):
        print(f"\n{self._enunciat}")
        for i, r in enumerate(self._respostes, 1):
            if r:
                print(f"  {i}. {r}")

    def demanar_resposta(self):
        opcions = [i + 1 for i, r in enumerate(self._respostes) if r]
        while True:
            try:
                r = int(input(f"Tria ({'/'.join(map(str, opcions))}): "))
                if r in opcions:
                    return r
            except ValueError:
                pass
            print("Resposta invàlida.")


def crear_pregunta(dades):
    """Factory: builds a Pregunta subclass from a DB row tuple."""
    id_p, id_q, tipus, enunciat, r1, r2, r3, r4, rc, punts = dades
    respostes = [r1 or "", r2 or "", r3 or "", r4 or ""]
    if tipus == "VF":
        return PreguntaVF(id_p, id_q, tipus, enunciat, respostes, rc, punts)
    return PreguntaMultiple(id_p, id_q, tipus, enunciat, respostes, rc, punts)
