from pregunta import Pregunta
class Questionari:
    
    def __init__(self, id_questionari:int, id_propietari:int, titol:str, categoria:str, dificultat: int, descripcio : str, preguntes: list[Pregunta]):
        self._id_questionari = id_questionari
        self._id_propietari = id_propietari
        self._titol = titol
        self._categoria = categoria
        self._dificultat = dificultat
        self._descripcio = descripcio
        self._preguntes = preguntes

    # GETTERS

    def get_id_questionari(self):
        return self.id_questionari

    def get_id_propietari(self):
        return self.id_propietari

    def get_titol(self):
        return self.titol

    def get_categoria(self):
        return self.categoria

    def get_dificultat(self):
        return self.dificultat

    def get_descripcio(self):
        return self.descripcio

    def get_preguntes(self):
        return self.preguntes

    # SETTERS

    def set_id_questionari(self, valor_nuevo):
        self.id_questionari = valor_nuevo
        return self.id_questionari

    def set_id_propietari(self, valor_nuevo):
        self.id_propietari = valor_nuevo
        return self.id_propietari

    def set_titol(self, valor_nuevo):
        self.titol = valor_nuevo
        return self.titol

    def set_categoria(self, valor_nuevo):
        self.categoria = valor_nuevo
        return self.categoria

    def set_dificultat(self, valor_nuevo):
        self.dificultat = valor_nuevo
        return self.dificultat

    def set_descripcio(self, valor_nuevo):
        self.descripcio = valor_nuevo
        return self.descripcio

    def set_preguntes(self, valor_nuevo):
        self.preguntes = valor_nuevo
        return self.preguntes
    
    def calcular_puntuacio(self):
        punts = 0
        for p in self._preguntes:
            punts += p.get_puntuacion()
        return punts