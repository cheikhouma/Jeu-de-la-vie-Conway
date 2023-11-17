# Jeu de la Vie de Conway

# Description
Le "Jeu de la Vie" est un automate cellulaire imaginé par John Conway en 1970.
Le Jeu de la vie est un « jeu à zéro joueur », puisqu'il ne nécessite aucune intervention du joueur lors de son déroulement. Il s’agit d’un automate cellulaire, un modèle où chaque état conduit mécaniquement à l’état suivant à partir de règles préétablies.

Le jeu se déroule sur une grille à deux dimensions, théoriquement infinie, dont les cases — appelées « cellules », par analogie avec les cellules vivantes — peuvent prendre deux états distincts : « vivante » ou « morte ».

Une cellule possède huit voisines, qui sont les cellules adjacentes horizontalement, verticalement et diagonalement.

À chaque itération, l'état d’une cellule est entièrement déterminée par l’état de ses huit cellules voisines, selon les règles suivantes :
Une chute de « bombes » non périodique.
une cellule morte possédant exactement trois cellules voisines vivantes devient vivante (elle naît) ;
une cellule vivante possédant deux ou trois cellules voisines vivantes le reste, sinon elle meurt.
Ainsi, la configuration  donne au tour suivant la configuration  qui redonne ensuite la première.
On peut également formuler cette évolution ainsi :
si une cellule a exactement trois voisines vivantes, elle est vivante à l’étape suivante.
C’est le cas de la cellule verte dans la configuration de gauche ;
si une cellule a exactement deux voisines vivantes, elle reste dans son état actuel à l’étape suivante.
Dans le cas de la configuration de gauche, la cellule située entre les deux cellules vivantes reste morte à l’étape suivante ;
si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle est morte à l’étape suivante.
C’est le cas de la cellule rouge dans la configuration de gauche.
L'état suivant d'une cellule est : (S = 3) OU (E = 1 ET S = 2).
Avec :
S : nombre actuel de cellules vivantes dans son voisinage (entier naturel compris entre 0 et 8 inclus) ;
E : état actuel de la cellule (entier naturel égal à 0 pour une cellule morte et égal à 1 pour une cellule vivante).
Il évolue au fil des générations en fonction d'un ensemble de règles simples.
Ce projet est une implémentation en Python du Jeu de la Vie, avec une interface graphique réalisée à l'aide de la bibliothèque Tkinter.


# Fonctionnalités

Grille Réactive : La grille s'ajuste automatiquement pour éviter les cellules partielles à la fin.
Contrôle du Jeu : Boutons "Start", "Pause" et "Reset" pour contrôler le déroulement du jeu.
Le bouton "Start" pour le demarrage du jeu et change en "Pause" quand le jeu demarre pour permettre a l'utilisateur d'arreter le jeu en un etat specifique.
Affichage des Itérations : Une étiquette affiche le nombre d'itérations pour suivre l'évolution du jeu pour une meilleure gestion du jeu.
Le bouton "Reset" permet de reinitialiser le jeu a l'etat d'origine c'est a dire iteration egale a zero et toutes les cellules mortes aussi
Crédit Développeur : Affichage d'une section de crédits du développeur qui peut etre aussi masquee.


# Installation

Assurez-vous d'avoir Python installé sur votre machine.
Clonez le dépôt : git clone https://github.com/cheikhouma/Jeu-de-la-vie-Conway.git
Accédez au répertoire : cd Jeu-de-la-Vie
Exécutez le script principal : python main.py
# Utilisation
Cliquez sur les cellules pour les faire naître ou les tuer.

Utilisez les boutons "Start", "Pause" et "Reset" pour contrôler le jeu.

Ajoutez des samples prédefinis pour voir des patterns intéressants.
# Auteur
Cheikh Oumar Diallo, eleve ingenieur a l'Ecole Polytechnique de Thies
# License
Ce projet est sous license Apache 2.0 - voir le fichier LICENSE pour plus de détails.
