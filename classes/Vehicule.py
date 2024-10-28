import sqlite3
class vehicule :
    def __init__(self, db_file):
        self.conn = self.create_connection(db_file)
        self.create_table()


