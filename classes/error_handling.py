import re
class DatabaseError(Exception):
    """Exception levée pour les erreurs liées à la base de données."""

    def __init__(self, message, code=None):
        """
        Initialise l'exception avec un message et un code d'erreur optionnel.

        :param message: Message d'erreur à afficher.
        :param code: Code d'erreur associé (optionnel).
        """
        super().__init__(message)
        self.code = code

    def __str__(self):
        if self.code:
            return f"{self.args[0]} (Code: {self.code})"
        return self.args[0]