import pygame, sys
from pygame.locals import *
from partie import *
from parametre import *
from affichage import *
from joueur import *
from background import *


pygame.init()

joueur = Joueur()
fond = Fond()
son = Sound()

tab_plateau = Plateau()
choix = 1
op = 2
mere = 0


while True:
	joueur = Joueur()
	laser = Laser()
	tab_plateau = Plateau()

	if choix == 1:#Menu
		son.playSong(2)
		choix = menu(fond)

	elif choix == 2:#Partie SOLO
		joueur = Joueur()
		tab_plateau = Plateau()
		partie = Jeu(fond, joueur, tab_plateau, son)
		choix = partie.partieSolo()

		joueur.clear()
		laser.clear()
		tab_plateau.clear()

	elif choix == 3:#OPTIONS
		choix = gestionParametres(fond, son, False)
		if choix == 0:
			choix = 1
		
	elif choix == 4:#Partie MULTI
		partie = Jeu(fond, joueur, tab_plateau, son)
		choix = partie.partieMulti()

		joueur.clear()
		laser.clear()
		tab_plateau.clear()