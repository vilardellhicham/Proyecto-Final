class Usuari:

    def __init__(self, id_usuari, nom, nom_usuari, contrassenya, email, data_registre, num_partides, victories, derrotes, empats, puntuacio_total):
        self._id_usuari = id_usuari
        self._nom = nom
        self._nom_usuari = nom_usuari
        self._contrassenya = contrassenya
        self._email = email
        self._data_registre = data_registre
        self._num_partides = num_partides
        self._victories = victories
        self._derrotes = derrotes
        self._empats = empats
        self._puntuacio_total = puntuacio_total

    # GETTERS
    def get_id_usuari(self):
        return self._id_usuari

    def get_nom(self):
        return self._nom

    def get_nom_usuari(self):
        return self._nom_usuari

    def get_contrassenya(self):
        return self._contrassenya

    def get_email(self):
        return self._email

    def get_data_registre(self):
        return self._data_registre

    def get_num_partides(self):
        return self._num_partides

    def get_victories(self):
        return self._victories

    def get_derrotes(self):
        return self._derrotes

    def get_empats(self):
        return self._empats

    def get_puntuacio_total(self):
        return self._puntuacio_total

    # SETTERS
    def set_id_usuari(self, valor):
        self._id_usuari = valor

    def set_nom(self, valor):
        self._nom = valor

    def set_nom_usuari(self, valor):
        self._nom_usuari = valor

    def set_contrassenya(self, valor):
        self._contrassenya = valor

    def set_email(self, valor):
        self._email = valor

    def set_data_registre(self, valor):
        self._data_registre = valor

    def set_num_partides(self, valor):
        self._num_partides = valor

    def set_victories(self, valor):
        self._victories = valor

    def set_derrotes(self, valor):
        self._derrotes = valor

    def set_empats(self, valor):
        self._empats = valor

    def set_puntuacio_total(self, valor):
        self._puntuacio_total = valor
