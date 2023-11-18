import tkinter as tk
import time
import random


# Les configurations predefinies. c'est en Anglais je n'ai pas pu traduire en francais par contrainte de temps.

Glider_Gun = [(1, 5), (1, 6), (2, 5), (2, 6), (11, 5), (11, 6), (11, 7), (12, 4), (12, 8), (13, 3), (13, 9), (14, 3), (14, 9), (15, 6), (16, 4), (16, 8), (17, 5), (17, 6), (17, 7), (18, 6), (21, 3), (21, 4), (21, 5), (22, 3), (22, 4), (22, 5), (23, 2), (23, 6), (25, 1), (25, 2), (25, 6), (25, 7), (35, 3), (35, 4), (36, 3), (36, 4)]

Pulsar = [(3, 5), (3, 6), (3, 7), (3, 11), (3, 12), (3, 13), (5, 3), (5, 8), (5, 10), (5, 15), (6, 3), (6, 8), (6, 10), (6, 15), (7, 3), (7, 8), (7, 10), (7, 15), (8, 5), (8, 6), (8, 7), (8, 11), (8, 12), (8, 13), (10, 5), (10, 6), (10, 7), (10, 11), (10, 12), (10, 13), (11, 3), (11, 8), (11, 10), (11, 15), (12, 3), (12, 8), (12, 10), (12, 15), (13, 3), (13, 8), (13, 10), (13, 15), (15, 5), (15, 6), (15, 7), (15, 11), (15, 12), (15, 13), (17, 5), (17, 6), (17, 7), (17, 11), (17, 12), (17, 13)]

Beacon = [(2, 2), (2, 3), (3, 2), (4, 5), (5, 4), (5, 5)]

Toad = [(2, 3), (2, 4), (2, 5), (3, 2), (3, 3), (3, 4)]

Blinker = [(1, 1), (1, 2), (1, 3)]

Acorn = [(1, 3), (2, 1), (2, 3), (4, 2), (5, 3), (6, 3), (7, 3)]

Pentadecathlon = [(3, 2), (4, 2), (5, 1), (5, 3), (6, 2), (7, 2), (8, 2), (9, 2), (10, 1), (10, 3)]

Lightweight_Spaceship = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 4), (5, 1), (5, 2), (5, 3), (5, 4)]

Middleweight_Spaceship = [(1, 3), (1, 4), (2, 1), (2, 2), (2, 4), (2, 5), (3, 1), (3, 5), (4, 2), (4, 3), (4, 4), (5, 3)]

Heavyweight_Spaceship = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 5), (3, 5), (4, 1), (4, 4), (5, 2), (5, 3), (5, 4)]

Block_laying_Switch_Engine = [(2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 3), (5, 2)]

Lightweight_C5_Orthogonal_Spaceship = [(1, 1), (1, 4), (2, 5), (3, 1), (3, 5), (4, 2), (4, 3), (4, 4)]

Puffer_1 = [(1, 3), (2, 1), (2, 2), (2, 3), (2, 6), (3, 6), (4, 1), (4, 5), (5, 3), (5, 4), (5, 5), (5, 6)]

Tumbler = [(1, 3), (1, 4), (2, 1), (2, 2), (2, 5), (2, 6), (3, 1), (3, 2), (3, 5), (3, 6), (4, 1), (4, 2), (4, 4), (4, 5), (5, 3), (5, 4)]

Gospers_Glider_Gun_variant = [(1, 5), (1, 6), (2, 5), (2, 6), (11, 5), (11, 6), (11, 7), (12, 4), (12, 8), (13, 3), (13, 9), (14, 3), (14, 9), (15, 6), (16, 4), (16, 8), (17, 5), (17, 6), (17, 7), (18, 6), (21, 3), (21, 4), (21, 5), (22, 3), (22, 4), (22, 5), (23, 2), (23, 6), (25, 1), (25, 2), (25, 6), (25, 7), (35, 3), (35, 4), (36, 3), (36, 4)]

Lightweight_Glider_Synthesizer = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 4), (3, 4), (4, 4)]

Block = [(1, 1), (1, 2), (2, 1), (2, 2)]

Beehive = [(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 3)]

Loaf = [(1, 2), (1, 3), (2, 1), (2, 4), (3, 2), (3, 4), (4, 3)]

Boat = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 2)]

Tub = [(1, 2), (2, 1), (2, 3), (3, 2)]

R_pentomino = [(1, 2), (1, 3), (2, 1), (2, 2), (3, 2)]

Diehard = [(1, 7), (2, 1), (2, 2), (3, 2), (3, 6), (3, 7), (3, 8)]

Acorn2 = [(2, 3), (3, 1), (3, 3), (5, 4), (6, 3), (7, 3), (8, 3)]

Pulsar2 = [(1, 5), (1, 6), (1, 7), (1, 11), (1, 12), (1, 13), (3, 3), (3, 8), (3, 10), (3, 15), (6, 3), (6, 8), (6, 10), (6, 15), (7, 3), (7, 8), (7, 10), (7, 15), (8, 5), (8, 6), (8, 7), (8, 11), (8, 12), (8, 13), (10, 5), (10, 6), (10, 7), (10, 11), (10, 12), (10, 13), (11, 3), (11, 8), (11, 10), (11, 15), (12, 3), (12, 8), (12, 10), (12, 15), (13, 3), (13, 8), (13, 10), (13, 15), (15, 5), (15, 6), (15, 7), (15, 11), (15, 12), (15, 13), (17, 5), (17, 6), (17, 7), (17, 11), (17, 12), (17, 13)]

Queen_bee_shuttle = [(1, 2), (1, 3), (1, 6), (1, 7), (2, 1), (2, 7), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (6, 1), (6, 7), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]


class JeuDeLaVieInterface:
    def __init__(self, taille_grille):
        self.taille_grille = taille_grille
        self.grille = [[0] * taille_grille for _ in range(taille_grille)]
        self.iteration = 0

        self.root = tk.Tk()
        self.root.title("Jeu de la Vie de CODIALLO")
        self.root.config()

        largeur_grille = taille_grille * 20
        largeur_boutons = 2 * 12 + 3 * 5
        largeur_fenetre = max(largeur_grille + largeur_boutons, 720)
        hauteur_fenetre = taille_grille * 20
        ecran_largeur = self.root.winfo_screenwidth()
        ecran_hauteur = self.root.winfo_screenheight()

        self.root.minsize(width=largeur_grille + largeur_boutons + 300, height=hauteur_fenetre + 20)

        x_position = (ecran_largeur - largeur_fenetre) // 2
        y_position = (ecran_hauteur - hauteur_fenetre) // 2

        self.root.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")

        self.canevas = tk.Canvas(self.root, width=largeur_fenetre, height=hauteur_fenetre)
        self.canevas.pack(side="left", expand=True)

        self.canevas.bind("<Button-1>", self.clique_cellule)

        # Les Boutons Reset et Start
        self.bouton_start_pause = tk.Button(self.root, text="Start", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", command=self.toggle_start_pause, width=12, height=1)
        self.bouton_start_pause.pack(side="top", pady=(10, 5), padx=10)

        self.bouton_reset = tk.Button(self.root, text="Reset", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", command=self.reset_jeu, width=12, height=1)
        self.bouton_reset.pack(side="top", pady=5, padx=10)

        # Creation du bouton de credit du developpeur
        self.bouton_credit = tk.Button(self.root, text="Masquer Credit", font=("Arial Black", 15), background="#000000", foreground="#FFFFFF", command=self.toggle_credit, width=12, height=1)
        self.bouton_credit.pack(side="bottom", padx=10, pady=15)
        self.credit_texte = tk.Label(text="This game is develooped\nby:\nCheikh Oumar Diallo\nComputer scientist \nstudent engineering\n at\n The Polytechnic School of \nThies\n", font=("Arial Black", 10), background="#FFFFFF", foreground="#000000", width=22, height=10)
        self.credit_texte.pack(side="bottom", expand=True, padx=5, pady=5)

        # Etat du bouton
        self.etat_credit = False

        # Étiquette pour afficher le nombre d'itérations
        self.etiquette_iteration = tk.Label(self.root, text=f"Iteration: {self.iteration}", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", width=12, height=2)
        self.etiquette_iteration.pack(side="top", pady=(5, 10), padx=5)

        # Bouton Aléatoire
        self.bouton_aleatoire = tk.Button(self.root, text="Aléatoire", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", command=self.choisir_configuration_aleatoire, width=12, height=1)
        self.bouton_aleatoire.pack(side="top", pady=(10, 5), padx=10)

        # Bouton Choisir par Nom
        self.bouton_choisir_nom = tk.Button(self.root, text="Configurations", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", command=self.choisir_configuration_par_nom, width=12, height=1)
        self.bouton_choisir_nom.pack(side="top", pady=5, padx=10)

        # Affichage de la grille
        self.afficher_grille()

        self.jeu_en_cours = False
        self.root.mainloop()

    def adjuster_taille_grille(self):
        largeur_effective = max([i for i in range(self.taille_grille) if any(self.grille[i])], default=0)
        nouvelle_taille = max(largeur_effective + 1, 5)

        if nouvelle_taille != self.taille_grille:
            self.taille_grille = nouvelle_taille
            self.grille = [[0] * self.taille_grille for _ in range(self.taille_grille)]

    def afficher_grille(self):
        self.canevas.delete("all")

        for i in range(self.taille_grille):
            for j in range(self.taille_grille):
                x1 = i * 20
                y1 = j * 20
                x2 = x1 + 20
                y2 = y1 + 20
                couleur = "black" if self.grille[i][j] == 1 else "white"
                self.canevas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")

    def clique_cellule(self, event):
        x = event.x // 20
        y = event.y // 20
        self.grille[x][y] = 1 - self.grille[x][y]  # Basculer entre 0 et 1
        self.afficher_grille()

    def toggle_start_pause(self):
        if self.jeu_en_cours:
            self.jeu_en_cours = False
            self.bouton_start_pause["text"] = "Start"
        else:
            self.jeu_en_cours = True
            self.bouton_start_pause["text"] = "Pause"
            self.jouer_jeu()

    # La fonction du bouton reset
    def reset_jeu(self):
        self.jeu_en_cours = False
        self.bouton_start_pause["text"] = "Start"
        self.grille = [[0] * self.taille_grille for _ in range(self.taille_grille)]
        self.iteration = 0
        self.etiquette_iteration["text"] = f"Iteration: {self.iteration}"
        self.afficher_grille()

    # Fonction d'affichage du credit du developpeur
    def toggle_credit(self):
        self.etat_credit = not self.etat_credit

        if self.etat_credit:
            self.credit_texte.pack_forget()
            self.bouton_credit["text"] = "Afficher credit"
        else:
            self.credit_texte.pack()
            self.bouton_credit["text"] = "Masquer credit"

    # Fonction principale du jeu

    def choisir_configuration_par_nom(self):
        noms_configurations = [
            "Glider Gun", "Pulsar", "Beacon", "Toad", "Blinker", "Acorn", "Pentadecathlon", "Lightweight Spaceship",
            "Middleweight Spaceship", "Heavyweight Spaceship", "Block-laying Switch Engine",
            "Lightweight C/5 Orthogonal Spaceship", "Puffer 1", "Tumbler", "Gosper's Glider Gun variant",
            "Lightweight Glider Synthesizer", "Block", "Beehive", "Loaf", "Boat", "Tub", "R-pentomino",
            "Diehard", "Acorn 2", "Pulsar 2", "Queen Bee Shuttle"]
        # Créer une fenêtre de sélection de configuration
        config_window = tk.Toplevel(self.root)
        config_window.title("Choisir une configuration")

        # Créer des boutons pour chaque configuration
        for nom_config in noms_configurations:
            bouton_config = tk.Button(config_window, text=nom_config, command=lambda nom=nom_config: self.choisir_config_par_nom(nom))
            bouton_config.pack()

    def choisir_config_par_nom(self, nom_config):
        configurations = {
            "Glider Gun": Glider_Gun,
            "Pulsar": Pulsar,
            "Beacon": Beacon,
            "Toad": Toad,
            "Blinker": Blinker,
            "Acorn": Acorn,
            "Pentadecathlon": Pentadecathlon,
            "Lightweight Spaceship": Lightweight_Spaceship,
            "Middleweight Spaceship": Middleweight_Spaceship,
            "Heavyweight Spaceship": Heavyweight_Spaceship,
            "Block-laying Switch Engine": Block_laying_Switch_Engine,
            "Lightweight C/5 Orthogonal Spaceship": Lightweight_C5_Orthogonal_Spaceship,
            "Puffer 1": Puffer_1,
            "Tumbler": Tumbler,
            "Gosper's Glider Gun variant": Gospers_Glider_Gun_variant,
            "Lightweight Glider Synthesizer": Lightweight_Glider_Synthesizer,
            "Block": Block,
            "Beehive": Beehive,
            "Loaf": Loaf,
            "Boat": Boat,
            "Tub": Tub,
            "R-pentomino": R_pentomino,
            "Diehard": Diehard,
            "Acorn 2": Acorn2,
            "Pulsar 2": Pulsar2,
            "Queen Bee Shuttle": Queen_bee_shuttle
        }

        configuration_choisie = configurations.get(nom_config)

        if configuration_choisie:
            self.grille = [[0] * self.taille_grille for _ in range(self.taille_grille)]

            for x, y in configuration_choisie:
                if 0 <= x < self.taille_grille and 0 <= y < self.taille_grille:
                    self.grille[x][y] = 1

            self.afficher_grille()

    def choisir_configuration_aleatoire(self):
        configurations = [
            Glider_Gun, Pulsar, Beacon, Toad, Blinker, Acorn, Pentadecathlon, Lightweight_Spaceship,
            Middleweight_Spaceship, Heavyweight_Spaceship, Block_laying_Switch_Engine,
            Lightweight_C5_Orthogonal_Spaceship, Puffer_1, Tumbler, Gospers_Glider_Gun_variant,
            Lightweight_Glider_Synthesizer, Block, Beehive, Loaf, Boat, Tub, R_pentomino,
            Diehard, Acorn2, Pulsar2, Queen_bee_shuttle]

        configuration_aleatoire = random.choice(configurations)

        self.grille = [[0] * self.taille_grille for _ in range(self.taille_grille)]

        for x, y in configuration_aleatoire:
            if 0 <= x < self.taille_grille and 0 <= y < self.taille_grille:
                self.grille[x][y] = 1

        self.afficher_grille()

    def jouer_jeu(self):
        if self.jeu_en_cours:
            nouvelle_grille = [[0] * self.taille_grille for _ in range(self.taille_grille)]

            for i in range(self.taille_grille):
                for j in range(self.taille_grille):
                    voisins_vivants = self.calculer_voisins_vivants(i, j)

                    if self.grille[i][j] == 1:
                        if voisins_vivants < 2 or voisins_vivants > 3:
                            nouvelle_grille[i][j] = 0
                        else:
                            nouvelle_grille[i][j] = 1
                    elif self.grille[i][j] == 0 and voisins_vivants == 3:
                        nouvelle_grille[i][j] = 1

            self.grille = nouvelle_grille
            self.afficher_grille()

            self.iteration += 1
            self.etiquette_iteration["text"] = f"Iteration: {self.iteration}"

            self.root.update_idletasks()
            self.root.update()
            time.sleep(0.1)

            self.root.after(100, self.jouer_jeu)

    def calculer_voisins_vivants(self, x, y):
        voisins = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < self.taille_grille and 0 <= ny < self.taille_grille:
                voisins += self.grille[nx][ny]

        return voisins


# Taille de la grille (par exemple, 36x36 pour une résolution minimale de 720x720)
taille_grille_globale = 36

# Créer l'interface graphique
interface_graphique = JeuDeLaVieInterface(taille_grille_globale)
