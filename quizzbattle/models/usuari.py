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
        return self.id_usuari

    def get_nom(self):
        return self.nom

    def get_nom_usuari(self):
        return self.nom_usuari

    def get_contrassenya(self):
        return self.contrassenya

    def get_email(self):
        return self.email

    def get_data_registre(self):
        return self.data_registre

    def get_num_partides(self):
        return self.num_partides

    def get_victories(self):
        return self.victories

    def get_derrotes(self):
        return self.derrotes

    def get_empats(self):
        return self.empats

    def get_puntuacio_total(self):
        return self.puntuacio_total

    # SETTERS

    def set_id_usuari(self, valor_nuevo):
        self.id_usuari = valor_nuevo
        return self.id_usuari

    def set_nom(self, valor_nuevo):
        self.nom = valor_nuevo
        return self.nom

    def set_nom_usuari(self, valor_nuevo):
        self.nom_usuari = valor_nuevo
        return self.nom_usuari

    def set_contrassenya(self, valor_nuevo):
        self.contrassenya = valor_nuevo
        return self.contrassenya

    def set_email(self, valor_nuevo):
        self.email = valor_nuevo
        return self.email

    def set_data_registre(self, valor_nuevo):
        self.data_registre = valor_nuevo
        return self.data_registre

    def set_num_partides(self, valor_nuevo):
        self.num_partides = valor_nuevo
        return self.num_partides

    def set_victories(self, valor_nuevo):
        self.victories = valor_nuevo
        return self.victories

    def set_derrotes(self, valor_nuevo):
        self.derrotes = valor_nuevo
        return self.derrotes

    def set_empats(self, valor_nuevo):
        self.empats = valor_nuevo
        return self.empats

    def set_puntuacio_total(self, valor_nuevo):
        self.puntuacio_total = valor_nuevo
        return self.puntuacio_total