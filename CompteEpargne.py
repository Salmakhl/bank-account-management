from Compte import Compte

class CompteEpargne(Compte):
    def __init__(self, numero, propriete, solde, date_ouverture, interet):
        super().__init__(numero, propriete, solde, date_ouverture)
        self.__interet = interet


    @property
    def get_interet(self):
        return self.__interet

    def __str__(self):
        return f"Compte n°{self.get_num}; Propriétaire: {self.get_propriete};\
Solde: {self.get_solde}; Date d'ouverture: {self.get_dateouver};\
Intérêt: {self.__interet}"
