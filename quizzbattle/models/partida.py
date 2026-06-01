import datetime
from models.questionari import Questionari


class Partida:

    def __init__(self, preguntes_encertades: list, preguntes_erroneas: list, jugadors: list, puntuacion_final: list, guanyador: str, questionari: Questionari, tipus: str, data: datetime.datetime):
        self._preguntes_encertades = preguntes_encertades
        self._preguntes_erroneas = preguntes_erroneas
        self._jugadors = jugadors
        self._puntuacion_final = puntuacion_final
        self._guanyador = guanyador
        self._questionari = questionari
        self._tipus = tipus
        self._data = data

    # GETTERS
    def get_preguntes_encertades(self):
        return self._preguntes_encertades

    def get_preguntes_erroneas(self):
        return self._preguntes_erroneas

    def get_jugadors(self):
        return self._jugadors

    def get_puntuacion_final(self):
        return self._puntuacion_final

    def get_guanyador(self):
        return self._guanyador

    def get_questionari(self):
        return self._questionari

    def get_tipus(self):
        return self._tipus

    def get_data(self):
        return self._data

    # SETTERS
    def set_preguntes_encertades(self, valor):
        self._preguntes_encertades = valor

    def set_preguntes_erroneas(self, valor):
        self._preguntes_erroneas = valor

    def set_jugadors(self, valor):
        self._jugadors = valor

    def set_puntuacion_final(self, valor):
        self._puntuacion_final = valor

    def set_guanyador(self, valor):
        self._guanyador = valor

    def set_questionari(self, valor):
        self._questionari = valor

    def set_tipus(self, valor):
        self._tipus = valor

    def set_data(self, valor):
        self._data = valor
