import tkinter as tk
import time


class JeuDeLaVieInterface:
    def __init__(self, taille_grille):
        self.taille_grille = taille_grille
        self.grille = [[0] * taille_grille for _ in range(taille_grille)]
        self.iteration = 0

        self.root = tk.Tk()
        self.root.iconbitmap("logo.ico")
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
        self.bouton_start_pause = tk.Button(self.root, text="Start", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", command=self.toggle_start_pause, width=12, height=2)
        self.bouton_start_pause.pack(side="top", pady=(10, 5), padx=10)

        self.bouton_reset = tk.Button(self.root, text="Reset", font=("Arial Black", 15), background="Blue", foreground="#FFFFFF", command=self.reset_jeu, width=12, height=2)
        self.bouton_reset.pack(side="top", pady=5, padx=10)

        # Creation du bouton de credit du developpeur
        self.bouton_credit = tk.Button(self.root, text="Masquer Credit", font=("Arial Black", 15), background="#000000", foreground="#FFFFFF", command=self.toggle_credit, width=15, height=3)
        self.bouton_credit.pack(side="bottom", padx=15, pady=15)
        self.credit_texte = tk.Label(text="Ce jeu est developpe\npar: Cheikh Oumar Diallo\neleve ingenieur a\nl'Ecole Polytechnique de Thies\nEn deuxieme annee\nOption Genie Informatique", font=("Arial Black", 10), background="#FFFFFF", foreground="#000000", width=28, height=15)
        self.credit_texte.pack(side="bottom", expand=True)

        # Etat du bouton
        self.etat_credit = False

        # Étiquette pour afficher le nombre d'itérations
        self.etiquette_iteration = tk.Label(self.root, text=f"Iteration: {self.iteration}", font=("Arial Black", 10), background="Blue", foreground="#FFFFFF", width=15, height=2)
        self.etiquette_iteration.pack(side="top", pady=(5, 10), padx=5)

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
