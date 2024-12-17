from functools import wraps

class Event:
    """
    Classe gérant les alertes et les événements liés au parking.
    """

    @staticmethod
    def log_event(func):
        """
        Décorateur pour enregistrer les actions dans un log.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} exécutée avec args={args} kwargs={kwargs}")
            return result
        return wrapper

    @staticmethod
    def alert(current_capacity, max_capacity):
        """
        Affiche des alertes en fonction de la capacité du parking.
        """
        if current_capacity >= 0.95 * max_capacity:
            print("Alerte : Le parking est presque plein (95%) !")
        elif current_capacity >= 0.80 * max_capacity:
            print("Alerte : Le parking est bientôt plein (80%).")

    @staticmethod
    def find_vehicles_by_type(vehicules, type):
        """
        Utilise une fonction lambda avec `filter` pour trouver les véhicules d'un type donné.
        """
        return list(filter(lambda v: v.type == type, vehicules))
