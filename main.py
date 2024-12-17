from classes.Vehicule import Vehicule
from classes.Event import Event
from classes.Parking import Parking
import random
import time

if __name__ == "__main__":
    # Initialisation
    mon_parking = Parking(20, "24/7", 2.5)
    mon_event = Event()

    for _ in range(10):  # Simulation sur 10 cycles
        new_vehicle = Vehicule.create_random_vehicule()
        print(f"\nNouveau véhicule : {new_vehicle.immatriculation} ({new_vehicle.type})")
        mon_parking.vehicules_entry(new_vehicle)

        # Sortie aléatoire
        if mon_parking._parking and random.choice([True, False]):
            vehicle_to_leave = random.choice(mon_parking._parking)
            mon_parking.vehicules_leave(vehicle_to_leave)

        # Alertes
        Event.alert(len(mon_parking._parking), mon_parking._capacity)

        time.sleep(1)  # Pause pour simuler le temps

    # Rapport final
    mon_parking.generate_report()

    # Recherche de véhicules par type
    voitures = Event.find_vehicles_by_type(mon_parking._parking, "voiture")
    print(f"Voitures stationnées : {[v.immatriculation for v in voitures]}")
