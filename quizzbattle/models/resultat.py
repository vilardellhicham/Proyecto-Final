class Resultat:

    def __init__(self, id_resultat, id_partida, id_usuari, puntuacio, resultat):
        self._id_resultat = id_resultat
        self._id_partida = id_partida
        self._id_usuari = id_usuari
        self._puntuacio = puntuacio
        self._resultat = resultat  # WIN, LOSE, DRAW

    # GETTERS
    def get_id_resultat(self):
        return self._id_resultat

    def get_id_partida(self):
        return self._id_partida

    def get_id_usuari(self):
        return self._id_usuari

    def get_puntuacio(self):
        return self._puntuacio

    def get_resultat(self):
        return self._resultat

    # SETTERS
    def set_puntuacio(self, valor):
        self._puntuacio = valor

    def set_resultat(self, valor):
        self._resultat = valor
