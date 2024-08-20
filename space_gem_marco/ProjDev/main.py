"""
Author : Marc Antoine Romao
Date : 20.08.2024
Objectif : Faire un jeu selon un modèle
"""

from pgzhelper import *
import pgzrun



"Taille fenetre"
WIDTH = 800
HEIGHT = 600

"Appel de l'image du spaceship dans la fenetre avec les coordonnées"
ship = Actor('playership1_blue')
ship.x = 370
ship.y = 550

"Mouvement A-D"
def update():
    if keyboard.a:
        ship.x -= 5
    if keyboard.d:
        ship.x += 5

def draw():
    screen.fill((80, 0, 70))  # Change la couleur d'arrière-plan
    ship.draw()

pgzrun.go()

