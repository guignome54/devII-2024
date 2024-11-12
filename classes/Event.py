class Event:

    def __init__(self):
        pass

    def alert(capacity, current_capacity, max_capacity):

        """
        PRE : reçoit la capacité actuelle du parking 
        POST : si le parking est remplit à 80% ou 95%, ouvre une fenêtre d'alerte
        """
        if current_capacity >= 0.95 * max_capacity:
            print("Alerte : Le parking est presque plein (95%) !")
        elif current_capacity >= 0.80 * max_capacity:
            print("Alerte : Le parking est bientôt plein (80%).")

    def change_tarif(self, parking, new_tarif):
        """
        PRE : reçoit le parking et le nouveau tarif
        POST : change le tarif actuel du parking
        """
        parking.tarif = new_tarif
        print(f"Le tarif a été mis à jour à {new_tarif}€.")