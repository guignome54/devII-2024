import sqlite3
from error_handling import DatabaseError
from Parking import Parking  # Fichier contenant la classe Parking
from interfaceGUI import InterfaceGUI  # Fichier contenant la classe InterfaceGUI

def main():
    # Crée une instance de Parking avec un fichier SQLite
    db_file = "parking.db"
    parking = Parking(db_file)  # Initialisation de la base de données

    # Lancement de l'interface graphique
    app = InterfaceGUI(parking)  # Passe l'instance de Parking à l'interface
    app.root.mainloop()  # Lance la boucle principale de Tkinter

if __name__ == "__main__":
    main()