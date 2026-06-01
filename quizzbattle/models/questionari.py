from models.pregunta import Pregunta


class Questionari:

    def __init__(self, id_questionari: int, id_propietari: int, titol: str, categoria: str, dificultat: int, descripcio: str, preguntes: list):
        self._id_questionari = id_questionari
        self._id_propietari = id_propietari
        self._titol = titol
        self._categoria = categoria
        self._dificultat = dificultat
        self._descripcio = descripcio
        self._preguntes = preguntes

    # GETTERS
    def get_id_questionari(self):
        return self._id_questionari

    def get_id_propietari(self):
        return self._id_propietari

    def get_titol(self):
        return self._titol

    def get_categoria(self):
        return self._categoria

    def get_dificultat(self):
        return self._dificultat

    def get_descripcio(self):
        return self._descripcio

    def get_preguntes(self):
        return self._preguntes

    # SETTERS
    def set_id_questionari(self, valor):
        self._id_questionari = valor

    def set_id_propietari(self, valor):
        self._id_propietari = valor

    def set_titol(self, valor):
        self._titol = valor

    def set_categoria(self, valor):
        self._categoria = valor

    def set_dificultat(self, valor):
        self._dificultat = valor

    def set_descripcio(self, valor):
        self._descripcio = valor

    def set_preguntes(self, valor):
        self._preguntes = valor

    def calcular_puntuacio(self):
        return sum(p.get_punts() for p in self._preguntes)
