import pygame, sys
from pygame.locals import *

class Fond:
	fond_partie = None
	i = 0
	tab_fonds = [
	(0, 255, 0),
	(0, 255, 255),
	(255, 0, 255),
	(255, 255, 0),
	(255, 255, 255)
	]

	def __init__(self):
		self.chargerFond()

	def chargerFond(self):
		self.fond_partie = self.tab_fonds[self.i]

	def initDict(self):
		sauvegarde_fond = open("liste_fonds.txt", 'r')
		for fond in sauvegarde_fond.readlines():
			id_fond = fond[:fond.index(':')]
			nom_fond = fond[fond.index(':')+1:fond.index('\n')]
			self.dict_fonds[id_fond] = nom_fond
		print(id_fond, nom_fond)
		sauvegarde_fond.close()

	def choixFond(self):
		LARGEUR = 640
		HAUTEUR = 480

		fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
		pygame.display.set_caption("Choix fond")

		font = pygame.font.Font(None, 40)
		
		y = HAUTEUR//2
		taille_triangle = 60
		
		self.chargerFond()

		while True:
			fenetre.fill(self.fond_partie)
			couleur = [255-self.tab_fonds[self.i][0], 255-self.tab_fonds[self.i][1], 255-self.tab_fonds[self.i][2]]
			texte = font.render("Choisissez votre couleur de fond", 1, couleur)
			terminer = font.render("Terminer", 1, couleur)
			fenetre.blit(texte, (LARGEUR//2-texte.get_width()//2, 10))
			terminer_p = fenetre.blit(terminer, (LARGEUR//2-terminer.get_width()//2, HAUTEUR-HAUTEUR//3+30))
			x = LARGEUR//3
			gauche = pygame.draw.polygon(fenetre, couleur, ((x, y), (x+taille_triangle, y-taille_triangle), (x+taille_triangle, y+taille_triangle)))
			x = LARGEUR - LARGEUR//3
			droite = pygame.draw.polygon(fenetre, couleur, ((x, y), (x-taille_triangle, y-taille_triangle), (x-taille_triangle, y+taille_triangle)))

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == MOUSEBUTTONDOWN:
					if event.pos[1] > gauche.y and event.pos[1] < gauche.y+gauche.h:
						if event.pos[0] > gauche.x and event.pos[0] < gauche.x+gauche.w:
							self.i -= 1
						elif event.pos[0] > droite.x and event.pos[0] < droite.x+droite.w:
							self.i += 1
					elif event.pos[0] > terminer_p.x and event.pos[0] < terminer_p.x+terminer_p.w and event.pos[1] > terminer_p.y and event.pos[1] < terminer_p.y+terminer_p.h:
						print("terminer")
						return 1

					if self.i > len(self.tab_fonds)-1:
						self.i = 0
					elif self.i < 0:
						self.i = len(self.tab_fonds)-1

					self.chargerFond()

			pygame.display.update()