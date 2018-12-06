import pygame, sys
from pygame.locals import *


class Joueur():
	x = 0
	y = 0
	niveau = None
	score = 0
	pose_choix = []
	poses_clic = []
	score = 0
	essais = 0

	def __init__(self, nom = "Joueur 1", niveau = 1):
		self.nom = nom
		self.niveau = niveau

	def clear(self):
		self.x = 0
		self.y = 0
		self.niveau = None
		self.score = 0
		self.pose_choix.clear()
		self.poses_clic.clear()
		self.score = 0
		self.essais = 0

		
	def coordonnees(self):
		fps = pygame.time.Clock()

		while True:

			event = pygame.event.wait()
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == MOUSEBUTTONDOWN:
				print("clic_2")
				# print(event.pos)
				return event.pos[0], event.pos[1], event.button
			elif event.type == MOUSEMOTION:
				return event.pos[0], event.pos[1], 0
			fps.tick(30)