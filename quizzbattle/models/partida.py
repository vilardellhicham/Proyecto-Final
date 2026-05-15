from questionari import Questionari
import datetime
class Partida:

    def __init__(self, preguntes_encertades:list, preguntes_erroneas:list, jugadors:list, puntuacion_final:list, guanyador:str, questionari:Questionari, tipus:str, data:datetime.datetime):
        
        self._preguntes_encertades = preguntes_encertades
        self._preguntes_erroneas = preguntes_erroneas
        self._jugadors = jugadors
        self._puntuacion_final = puntuacion_final
        self._guanyador = guanyador
        self._questionari = questionari
        self._tipus = tipus #tipo de modo de juego
        self._data = data #fecha

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

    def set_preguntes_encertades(self, valor_nuevo):
        self._preguntes_encertades = valor_nuevo
        return self._preguntes_encertades

    def set_preguntes_erroneas(self, valor_nuevo):
        self._preguntes_erroneas = valor_nuevo
        return self._preguntes_erroneas

    def set_jugadors(self, valor_nuevo):
        self._jugadors = valor_nuevo
        return self._jugadors

    def set_puntuacion_final(self, valor_nuevo):
        self._puntuacion_final = valor_nuevo
        return self._puntuacion_final

    def set_guanyador(self, valor_nuevo):
        self._guanyador = valor_nuevo
        return self._guanyador

    def set_questionari(self, valor_nuevo):
        self._questionari = valor_nuevo
        return self._questionari

    def set_tipus(self, valor_nuevo):
        self._tipus = valor_nuevo
        return self._tipus

    def set_data(self, valor_nuevo):
        self._data = valor_nuevo
        return self._data