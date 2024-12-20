from dataclasses import dataclass


@dataclass
class Emplacement:
    """
    Classe représentant un emplacement dans un parking.
    """
    type: str
    is_available: bool = True
    position: tuple = (0, 0)

    def manage_emplacement(self, vehicule):
        """
        Gère l'entrée ou la sortie d'un véhicule de l'emplacement.
        """
        if self.is_available:
            self.is_available = False
            vehicule.is_parked = True
            print(f"Véhicule {vehicule.immatriculation} garé à la position {self.position}.")
        else:
            self.is_available = True
            vehicule.is_parked = False
            print(f"Véhicule {vehicule.immatriculation} a quitté la position {self.position}.")
