class Compte:
    def __init__(self, numero, propriete, solde, date_ouverture):
        self.__numero = numero
        self.__propriete = propriete
        self.__solde = solde
        self.__date_ouverture = date_ouverture


    @property
    def get_numero(self):
        return self.__numero

    @property
    def get_propriete(self):
        return self.__propriete

    @property
    def get_solde(self):
        return self.__solde

    @property
    def get_date(self):
        return self.__date_ouverture


    def __str__(self):
        return f"Compte n°{self.__numero}; Propriétaire: {self.__propriete};\
Solde: {self.__solde}; Date d'ouverture: {self.__date_ouverture}"
