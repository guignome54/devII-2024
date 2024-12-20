import random
from dataclasses import dataclass
import datetime


@dataclass
class Vehicule:
    """
    Classe représentant un véhicule.
    """
    immatriculation: str
    type: str  # "voiture", "moto", etc.
    is_parked: bool = False
    entry_time: datetime = None

    @staticmethod
    def create_random_vehicule():
        immatriculation = (f"{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
                           f"-{random.randint(100, 999)}"
                           f"-{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}")
        type = random.choice(["voiture", "moto", "camion"])
        return Vehicule(immatriculation, type)
    def __str__(self) :
        return (f"Type de véhicule : {self.type}\n"
                f"Immatriculation : {self.immatriculation}\n"
                f"Est garé ? : {self.is_parked}\n"
                f"Heure d'entrée : {self.entry_time}")
