class Pregunta:
    def __init__(self, enunciado, respuesta, puntuacion):
        self._enunciado = enunciado
        self._respuesta= respuesta
        self._puntuacion = puntuacion

    def validar_respuesta(self,respuesta_user):
        if respuesta_user==self._respuesta:
            return True
        else:
            return False

    # GETTERS

    def get_enunciado(self):
        return self._enunciado

    def get_respuesta(self):
        return self._respuesta

    def get_puntuacion(self):
        return self._puntuacion

    # SETTERS

    def set_enunciado(self, valor_nuevo):
        self._enunciado = valor_nuevo
        return self._enunciado

    def set_respuesta(self, valor_nuevo):
        self._respuesta = valor_nuevo
        return self._respuesta

    def set_puntuacion(self, valor_nuevo):
        self._puntuacion = valor_nuevo
        return self._puntuacion