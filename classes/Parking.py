import classes.Vehicule as vehicule
import classes.Emplacement as emplacement
import classes.Event as event

class Parking:

    def __init__(self, capacity, horaires, tarif):

        self.capacity = capacity
        self.horaires = horaires
        self.tarif = tarif

    def vehicules_entry(self, vehicule):

        """
        PRE : reçoit en entrée une instance de véhicule
        POST : enregistre l'instance et définis si il est parqué
        """

        return
    
    def vehicules_leave(self, vehicule):

        """
        PRE : reçoit en entrée une instance d'un véhicule dans le parking
        POST : l'instance quitte le parking
        """

        return
    
    def payements_history(self, payement):

        """
        PRE : reçoit un historique de payement
        POST : 
        """