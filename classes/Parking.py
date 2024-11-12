import Emplacement as emplacement
from datetime import datetime

class Parking:

    def __init__(self, capacity, horaires, tarif):
        self._parking = []
        self.capacity = capacity
        self.horaires = horaires
        self.tarif = tarif
        self._emplacements = [emplacement.Emplacement(type="regular")]
        self.payements = []

    def vehicules_entry(self, vehicule):

        """
        PRE : reçoit en entrée une instance de véhicule
        POST : enregistre l'instance et définis si il est parqué
        """
        for place in range(self.capacity) :
            self._emplacements.append(emplacement.Emplacement("regular"))
        for emplacement in self._emplacements:
            if emplacement.is_available:
                emplacement.manage_emplacement(vehicule)
                vehicule.entry_time = datetime.now()
                self._parking.append(vehicule)
                return
        print("Pas de places disponibles.")
    
    def vehicules_leave(self, vehicule):

        """
        PRE : reçoit en entrée une instance d'un véhicule dans le parking
        POST : l'instance quitte le parking
        """
        if vehicule in self._parking:
            duration = datetime.now() - vehicule.entry_time
            cost = self.calculate_tarif(duration)
            emplacement = next(e for e in self._emplacements if not e.is_available)
            emplacement.manage_emplacement(vehicule)
            print(f"Véhicule {vehicule.immatriculation} sorti. Coût : {cost:.2f}€.")
            self.register_payment(cost)
            self._parking.remove(vehicule)

    def calculate_tarif(self, duration):
        hours = duration.total_seconds() / 3600
        return self.tarif * hours
    
    def register_payment(self, amount, method="carte"):
        """
        Enregistre un paiement
        """
        payment = {"amount": amount, "method": method, "date": datetime.now()}
        self.payements.append(payment)
        print(f"Paiement enregistré : {amount}€ par {method}.")

    def generate_report(self):
        """
        Génère un rapport sur la fréquentation et les paiements
        """
        print(f"Rapport de fréquentation : {len(self._parking)} véhicules actuellement stationnés.")
        total = sum(p["amount"] for p in self.payements)
        print(f"Total des paiements enregistrés : {total}€.")