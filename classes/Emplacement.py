class Emplacement:

    def __init__(self, type , is_available = True, position = []):
        self.position = position
        self.type = type
        self.is_available = is_available


    def manage_emplacement(self, vehicule):
         """
         PRE : Reçois un véhicule en entrée
         POST : Ajoute ou retire la voiture de l'emplacement
         """
         if self.is_available:
            self.is_available = False
            vehicule.is_parked = True
            print(f"Véhicule {vehicule.immatriculation} garé.")
         else:
            self.is_available = True
            vehicule.is_parked = False
            print(f"Véhicule {vehicule.immatriculation} a quitté l'emplacement.")
         return
        
