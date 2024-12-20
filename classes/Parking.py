import re
from datetime import datetime
from classes.Emplacement import Emplacement
import random


class Parking:
    """
    Classe représentant un parking.
    """

    def __init__(self, capacity, horaires, tarif):
        self._capacity = capacity
        self._horaires = horaires
        self._tarif = tarif
        self.parking = []
        self._emplacements = [Emplacement("regular", position=(i, random.randint(0, 9))) for i in range(capacity)]
        self._payements = []

    @property
    def tarif(self):
        return self._tarif

    @tarif.setter
    def tarif(self, new_tarif):
        if new_tarif < 0:
            raise ValueError("Le tarif ne peut pas être négatif.")
        self._tarif = new_tarif

    def vehicules_entry(self, vehicule):
        """
        Enregistre l'entrée d'un véhicule dans le parking.
        Utilisation d'une expression régulière pour valider les immatriculations.
        """
        if not re.match(r"[A-Z]-\d{3}-[A-Z]", vehicule.immatriculation):
            print(f"Erreur : Immatriculation invalide pour {vehicule.immatriculation}.")
            return

        for emplacement in self._emplacements:
            if emplacement.is_available:
                emplacement.manage_emplacement(vehicule)
                vehicule.entry_time = datetime.now()
                self.parking.append(vehicule)
                return
        print("Pas de places disponibles.")

    def vehicules_leave(self, vehicule):
        """
        Enregistre la sortie d'un véhicule.
        """
        if vehicule not in self.parking:
            print("Erreur : Ce véhicule n'est pas dans le parking.")
            return

        duration = datetime.now() - vehicule.entry_time
        cost = self.calculate_tarif(duration)

        emplacement = next(e for e in self._emplacements if not e.is_available)
        emplacement.manage_emplacement(vehicule)

        print(f"Véhicule {vehicule.immatriculation} sorti. Coût : {cost:.2f}€.")
        self.register_payment(cost)
        self.parking.remove(vehicule)

    def calculate_tarif(self, duration):
        hours = duration.total_seconds() / 3600
        return self._tarif * hours

    def register_payment(self, amount, method="carte"):
        """
        Enregistre un paiement.
        """
        payment = {"amount": amount, "method": method, "date": datetime.now()}
        self._payements.append(payment)
        print(f"Paiement enregistré : {amount}€ par {method}.")

    def generate_report(self):
        """
        Génère un rapport détaillé.
        Utilise `map` pour extraire des données spécifiques.
        """
        print(f"\n--- Rapport de Parking ---")
        print(f"Véhicules actuellement stationnés : {len(self.parking)}")

        total = sum(map(lambda p: p["amount"], self._payements))
        print(f"Total des paiements : {total:.2f}€")

        payment_methods = {p["method"] for p in self._payements}
        print(f"Méthodes de paiement utilisées : {', '.join(payment_methods)}")
