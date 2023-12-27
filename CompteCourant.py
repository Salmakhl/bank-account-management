from Compte import Compte

class CompteCourant(Compte):
    def __init__(self, numero, propriete, solde, dateouver, montant):
        super().__init__(numero, propriete, solde, dateouver)
        self.__montant = montant


    @property
    def get_montant(self):
        return self.__montant


    def __str__(self):
        return f"Compte n°{self.get_numero}; Propriétaire: {self.get_propriete};\
Solde: {self.get_solde}; Date d'ouverture: {self.get_dateouver};\
Montant de couverture autorisé: {self.__montant}"
