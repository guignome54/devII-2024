from classes.Vehicule import Vehicule
from classes.Event import Event
from classes.Parking import Parking
import random
import time

if __name__ == "__main__":
    # Initialisation
    mon_parking = Parking(20, "24/7", 2.5)
    mon_event = Event()

    for _ in range(10):  # Nombre de cycles de simulation
        # Créer aléatoirement de nouveaux véhicules
        new_vehicle = Vehicule.create_random_vehicule()
        print(f"\nNouveau véhicule : {new_vehicle.immatriculation} ({new_vehicle.type})")
        mon_parking.vehicules_entry(new_vehicle)

        # Aléatoirement faire sortir certains véhicules
        if mon_parking._parking and random.choice([True, False]):  # 50% chance de sortie
            vehicle_to_leave = random.choice(mon_parking._parking)
            mon_parking.vehicules_leave(vehicle_to_leave)

        # Afficher les alertes de capacité
        Event.alert(len(mon_parking._parking), mon_parking.capacity)

        # Pause pour simuler le passage du temps
        time.sleep(1)

    # Rapport final
    mon_parking.generate_report()
