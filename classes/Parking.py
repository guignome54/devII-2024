import sqlite3
from error_handling import DatabaseError

class Parking:
    def __init__(self, db_file):
        # Initialisation de la connexion à la base de données et création de la table
        self.conn = self.create_connection(db_file)
        self.create_table()

    def create_connection(self, db_file):
        """Crée une connexion à la base de données SQLite."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print("Connexion établie à la db")
            return conn
        except sqlite3.Error as e:
            raise DatabaseError("Erreur de connexion à la base de données", e)

    def create_table(self):
        """Crée la table 'parking' si elle n'existe pas encore."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS parking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            immatriculation VARCHAR 
        );
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(create_table_sql)
            self.conn.commit()
            print("Table 'parking' créée ou existe déjà.")
        except sqlite3.Error as e:
            raise DatabaseError("Erreur lors de la création de la table 'parking'", e)

    def ajouter_voiture(self, immatriculation) :
        sql = '''INSERT INTO parking(immatriculation)
                 VALUES(?)'''
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, (immatriculation,))
            self.conn.commit()
            print(f"Plaque {immatriculation} ajouté à la base de données.")
        except sqlite3.Error as e:
            raise DatabaseError("Erreur lors de l'ajout de l'animal à la base de données", e)
        
    def consulter_voiture(self, id=None):
        """Récupère une voiture par ID ou toutes les voitures si aucun ID n'est fourni."""
        cursor = self.conn.cursor()
        if id:
            query = "SELECT * FROM parking WHERE id = ?"
            cursor.execute(query, (id,))
        else:
            query = "SELECT * FROM parking"
            cursor.execute(query)
    
        voitures = cursor.fetchall()
        if not voitures and id:
            raise DatabaseError(f"Aucune voiture trouvée avec l'ID : {id}")
        return voitures