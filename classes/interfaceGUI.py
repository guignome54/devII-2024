import tkinter as tk
from tkinter import messagebox, simpledialog
from error_handling import *

class InterfaceGUI :
    def __init__(self, Parking):
        self.Parking = Parking
        self.root = tk.Tk()
        self.root.title("Gestion Parking")
        self.label = tk.Label(self.root, text="Bienvenue dans l'interface de gestion")
        self.label.pack(padx=20, pady=20)
        tk.Button(self.root, text="Ajouter Voiture", command=self.ajouter_voiture_gui).pack(pady=5)
        tk.Button(self.root, text="Consulter Voiture", command=self.consulter_parking_gui).pack(pady=5)

    def ajouter_voiture_gui(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("ajouter voiture")

        frame = tk.Frame(new_window)
        frame.pack(padx=10, pady=10)                

        tk.Label(frame,text="Immatriculation:").grid(row=0)

        immatriculation = tk.Entry(frame)
        
        immatriculation.grid(row=0,column=1)
        def submit():
            try:
                self.Parking.ajouter_voiture(immatriculation.get())
                messagebox.showinfo("Succès", "Voiture ajouté avec succès!")
                new_window.destroy()
            except DatabaseError as e:
                messagebox.showerror("Erreur de base de données", str(e))
        tk.Button(frame, text="Ajouter", command=submit).grid(row=4, column=1, pady=10)
    
    def consulter_parking_gui(self):
        """Ouvre une fenêtre pour consulter les voitures dans le parking."""
        new_window = tk.Toplevel(self.root)
        new_window.title("Consulter Voitures")

        frame = tk.Frame(new_window)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="ID Voiture (laisser vide pour tout voir) :").grid(row=0, column=0)
        id_voiture = tk.Entry(frame)
        id_voiture.grid(row=0, column=1)

        def submit():
            try:
                id_value = id_voiture.get()
                voitures = self.Parking.consulter_voiture(int(id_value) if id_value else None)
            
                # Efface les widgets existants avant d'afficher les résultats
                for widget in frame.winfo_children():
                    widget.destroy()

                tk.Label(frame, text="ID | Immatriculation").grid(row=0, column=0, columnspan=2)
            
                # Affiche chaque voiture retournée
                for i, voiture in enumerate(voitures, start=1):

                    tk.Label(frame, text=" | ".join(map(str, voiture))).grid(row=i, column=0, columnspan=2)

            except DatabaseError as e:
                messagebox.showerror("Erreur", str(e))

        tk.Button(frame, text="Consulter", command=submit).grid(row=1, column=1, pady=10)