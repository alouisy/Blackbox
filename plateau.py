import copy, pygame, random
from pygame.locals import *
from background import Fond
from AnimLose import *
from gagne import *
from lose import *
from win import *

class Plateau():
	plateau_ref = []
	plateau_jeu = []
	plateau_pose = []
	coord_laser = []
	historique_coord_laser = []
	tab_message = []
	tab_atomes = []
	verti = False
	hori = False
	taille_carreau = 30
	taille_atome = taille_carreau//10
	taille_laser = taille_carreau//10
	nb_atomes = 0
	nb_cases = 0
	fenetre = None
	pose_x = 0
	pose_y = 0
	pose_v = 0
	pose_w = 0
	vu_laser = True
	compteur_coups = 0
	compteur_partie = 0
	deplacement = 0
	op = 2
	message = ""
	niveau = 0
	couleur_fond = None
	win = True
	joueur = None
	vu_atomes = False

	def __init__(self):
		pass

	def creaTab(self, nbCases = 5):
		
		self.nb_cases = nbCases+2
		tab = []

		self.plateau_ref = [[0]*self.nb_cases for i in range(self.nb_cases)]
		self.plateau_pose = [[0]*self.nb_cases for i in range(self.nb_cases)]
		self.tab_message = [[[]for j in range(self.nb_cases)]for i in range(4)]

		for colonne in range(self.nb_cases):
			for ligne in range(self.nb_cases):
				if ((colonne == 0 or colonne == self.nb_cases-1) and ligne > 0 and ligne < self.nb_cases-1) or (colonne > 0 and colonne < self.nb_cases-1 and (ligne == self.nb_cases-1 or ligne == 0)):
					self.plateau_ref[colonne][ligne] = 1
				elif (colonne > 0 and colonne < self.nb_cases-1 and ligne > 0 and ligne < self.nb_cases-1):
					self.plateau_ref[colonne][ligne] = 2

		self.plateau_jeu = copy.deepcopy(self.plateau_ref)

	def copy_plateau(self, tab_plateau):
		for i, ligne in enumerate(tab_plateau):
			for j, val in enumerate(ligne):
				self.plateau_ref[i][j] = val
				self.plateau_jeu[i][j] = val

	def set_joueur(self, joueur):
		self.joueur = joueur

	def clear(self):

		self.plateau_ref.clear()
		self.plateau_jeu.clear()
		self.plateau_pose.clear()
		self.coord_laser.clear()
		self.historique_coord_laser.clear()
		self.tab_message.clear()
		self.tab_atomes.clear()
		self.verti = False
		self.hori = False
		self.taille_carreau = 30
		self.taille_atome = self.taille_carreau//10
		self.taille_laser = self.taille_carreau//10
		self.nb_atomes = 0
		self.nb_cases = 0
		self.fenetre = None
		self.pose_x = 0
		self.pose_y = 0
		self.pose_v = 0
		self.pose_w = 0
		self.vu_laser = True
		self.compteur_coups = 0
		self.compteur_partie = 0
		self.deplacement = 0
		self.op = 2
		self.message = ""
		self.niveau = 0
		self.couleur_fond = None
		self.win = True
		self.joueur = None
		self.vu_atomes = False


	def affiche_laser(self, coord_laser = []):
		if self.op > 0:
			if self.op > 1 and self.vu_laser == True:
				pygame.draw.lines(self.fenetre, (255, 255, 0), False, coord_laser, self.taille_laser)

			if self.pose_w == 0:
				self.plateau_jeu[self.pose_w][self.pose_v] = 6 
				haut = pygame.draw.polygon(self.fenetre, (255, 255, 0), ((self.plateau_pose[self.pose_w][self.pose_v].centerx, self.plateau_pose[self.pose_w][self.pose_v].centery-self.taille_carreau//6),(self.plateau_pose[self.pose_w][self.pose_v].centerx-self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery+self.taille_carreau//6), (self.plateau_pose[self.pose_w][self.pose_v].centerx+self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery+self.taille_carreau//6)))

			elif self.pose_v == (len(self.plateau_jeu)-1):
				self.plateau_jeu[self.pose_w][self.pose_v] = 6 
				droite = pygame.draw.polygon(self.fenetre, (255, 255, 0), ((self.plateau_pose[self.pose_w][self.pose_v].centerx+self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery),(self.plateau_pose[self.pose_w][self.pose_v].centerx-self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery-self.taille_carreau//6), (self.plateau_pose[self.pose_w][self.pose_v].centerx-self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery+self.taille_carreau//6)))

			elif self.pose_v == 0:
				self.plateau_jeu[self.pose_w][self.pose_v] = 6 
				gauche = pygame.draw.polygon(self.fenetre, (255, 255, 0), ((self.plateau_pose[self.pose_w][self.pose_v].centerx-self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery),(self.plateau_pose[self.pose_w][self.pose_v].centerx+self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery-self.taille_carreau//6), (self.plateau_pose[self.pose_w][self.pose_v].centerx+self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery+self.taille_carreau//6)))

			elif self.pose_w == (len(self.plateau_jeu)-1):
				self.plateau_jeu[self.pose_w][self.pose_v] = 6 
				bas = pygame.draw.polygon(self.fenetre, (255, 255, 0), ((self.plateau_pose[self.pose_w][self.pose_v].centerx, self.plateau_pose[self.pose_w][self.pose_v].centery+self.taille_carreau//6),(self.plateau_pose[self.pose_w][self.pose_v].centerx-self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery-self.taille_carreau//6), (self.plateau_pose[self.pose_w][self.pose_v].centerx+self.taille_carreau//6, self.plateau_pose[self.pose_w][self.pose_v].centery-self.taille_carreau//6)))


	def affiche_clic(self):

		for coordonne in self.joueur.poses_clic:
			i = coordonne[0]
			j = coordonne[1]
			op = self.plateau_jeu[i][j]

			if op == 8:
				pygame.draw.rect(self.fenetre, (0, 0, 255), (self.plateau_pose[i][j].x, self.plateau_pose[i][j].y, self.taille_carreau, self.taille_carreau))
			if op == 6:
				pygame.draw.rect(self.fenetre, (0, 255, 0), (self.plateau_pose[i][j].x, self.plateau_pose[i][j].y, self.taille_carreau, self.taille_carreau))
			if op == 0:
				pygame.draw.rect(self.fenetre, (255, 255, 0), (self.plateau_pose[i][j].centerx-self.taille_carreau//6, self.plateau_pose[i][j].centery-self.taille_carreau//6, self.taille_carreau//3, self.taille_carreau//3))
			elif op == 1:
				pygame.draw.rect(self.fenetre, (0, 0, 255), (self.plateau_pose[i][j].x, self.plateau_pose[i][j].y, self.taille_carreau, self.taille_carreau))
			if op == 1:
				pygame.draw.rect(self.fenetre, (255, 0, 0), (self.plateau_pose[i][j].x, self.plateau_pose[i][j].y, self.taille_carreau, self.taille_carreau))
			elif op == 2 or op == 5:
				pygame.draw.rect(self.fenetre, (0, 0, 0), (self.plateau_pose[i][j].x, self.plateau_pose[i][j].y, self.taille_carreau, self.taille_carreau))
			elif op == 3 or self.plateau_ref[i][j] == 3:
				pygame.draw.circle(self.fenetre, (0, 255, 255), (self.plateau_pose[i][j].x+self.taille_carreau//2, self.plateau_pose[i][j].y+self.taille_carreau//2), self.taille_carreau//3)
			elif op == 4:
				pygame.draw.rect(self.fenetre, (255, 255, 0), (self.plateau_pose[i][j].centerx-self.taille_carreau//6, self.plateau_pose[i][j].centery-self.taille_carreau//6, self.taille_carreau//3, self.taille_carreau//3))
			elif op == 7:
				pygame.draw.rect(self.fenetre, (255, 0, 0), (self.plateau_pose[i][j].x, self.plateau_pose[i][j].y, self.taille_carreau, self.taille_carreau))


	def affiche_message(self):

		font = pygame.font.Font(None, 24)
		tours = 1
		if self.plateau_ref[self.pose_w][self.pose_v] == 1:
			tours = 2

		x = 0
		y = 0

		for i, bord in enumerate(self.tab_message):
			for j, messages in enumerate(bord):

				if i == 1:
					x = 0
				elif i == 2:
					x = self.nb_cases-1
				else:
					x = j

				if i == 0:
					y = 0
				elif i == 3:
					y = self.nb_cases-1
				else:
					y = j
				
				if self.plateau_pose[y][x] == 0:
					continue

				for k in range(len(messages)):

					if messages[k] != None:

						if x == 0:
							self.fenetre.blit(font.render(messages[k], 1, (0,0,255)), (self.plateau_pose[y][x].x-((self.taille_carreau*(k+1)+5)-self.taille_carreau//2), self.plateau_pose[y][x].y+self.taille_carreau//3))

						elif x == self.nb_cases-1:
							self.fenetre.blit(font.render(messages[k], 1, (0,0,255)), (self.plateau_pose[y][x].x+(self.taille_carreau*(k+1)), self.plateau_pose[y][x].y+self.taille_carreau//3))

						elif y == 0:
							self.fenetre.blit(font.render(messages[k], 1, (0,0,255)), (self.plateau_pose[y][x].x+self.taille_carreau//3, self.plateau_pose[y][x].y-((self.taille_carreau*(k+1))-self.taille_carreau//2)))

						elif y == self.nb_cases-1:
							self.fenetre.blit(font.render(messages[k], 1, (0,0,255)), (self.plateau_pose[y][x].x+self.taille_carreau//3, self.plateau_pose[y][x].y+(self.taille_carreau*(k+1))))

		self.message = ""


	def gestion_message(self):

		poses = (0, self.nb_cases-1)

		if self.message == "":
			self.message = str(self.compteur_coups)
		else:
			self.compteur_coups -= 1

		if self.pose_y == 0:
			self.tab_message[0][self.pose_x].append(self.message)

		elif self.pose_x == 0:
			self.tab_message[1][self.pose_y].append(self.message)

		elif self.pose_x == self.nb_cases-1:
			self.tab_message[2][self.pose_y].append(self.message)

		elif self.pose_y == self.nb_cases-1:
			self.tab_message[3][self.pose_x].append(self.message)

		if self.pose_v in poses or self.pose_w in poses:

			if self.pose_w == 0:
				self.tab_message[0][self.pose_v].append(self.message)

			elif self.pose_v == 0:
				self.tab_message[1][self.pose_w].append(self.message)

			elif self.pose_v == self.nb_cases-1:
				self.tab_message[2][self.pose_w].append(self.message)

			elif self.pose_w == self.nb_cases-1:
				self.tab_message[3][self.pose_v].append(self.message)


	def atomesAlea(self):
		nb_atomes = self.nb_atomes

		while nb_atomes != 0:
			poser_atome = True
			x = random.randint(1, self.nb_cases-2)
			y = random.randint(1, self.nb_cases-2)

			for i in range(y-1, y+2):
				for j in range(x-1, x+2):
					if self.plateau_ref[i][j] == 3:
						poser_atome = False
			if poser_atome == True:
				self.plateau_ref[y][x] = 3
				self.plateau_jeu[y][x] = 3
				self.tab_atomes.append((y, x))
				nb_atomes -= 1


	def afficheTableau(self, plateau, fenetre, taille_carreau):

		x = 0
		y = taille_carreau*3

		for i in range(len(plateau)):
			x = taille_carreau
			for j in range(len(plateau)):

				x += taille_carreau+2
				if(plateau[i][j] != 0):
					pygame.draw.rect(fenetre, (0, 0, 0), (x, y, taille_carreau, taille_carreau))
					if (i == 0) or (i == len(plateau)-1) or (j == 0) or (j == len(plateau)-1):
						pygame.draw.rect(fenetre, (255, 0, 0), (x, y, taille_carreau, taille_carreau))
					elif plateau[i][j] == 6:
						pygame.draw.rect(fenetre, (0, 255, 0), (x, y, taille_carreau, taille_carreau))
					elif plateau[i][j] == 7:
						pygame.draw.rect(fenetre, (255, 0, 0), (x, y, taille_carreau, taille_carreau))
					elif plateau[i][j] == 3 and self.vu_atomes == True:
						pygame.draw.circle(fenetre, (0, 255, 255), (x+15, y+15), 10)
			y += taille_carreau+2


	def animation1(self):
		FPS = pygame.time.Clock()
		fps = 10

		while fps < 120:

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			self.afficheTableau(self.plateau_ref, self.fenetre, self.taille_carreau)
			for i in range(random.randint(5, 25)):
				rand1 = random.randint(1, self.nb_cases-2)
				rand2 = random.randint(1, self.nb_cases-2)
				pygame.draw.rect(self.fenetre, (255, 0, 255), (self.plateau_pose[rand1][rand2].x, self.plateau_pose[rand1][rand2].y, self.taille_carreau, self.taille_carreau))

			fps += 1
			pygame.display.update()
			FPS.tick(fps)

	def gestionScore(self, pose_choix):
		score = 1000

		print("score_1", print(score))

		bon, mauvais = self.verificationPlateau(pose_choix)

		if self.vu_laser == True:
			score = score/2

		print("score_2", print(score))

		score -= (len(self.joueur.poses_clic)*(score//10))

		print("score_3", print(score))

		score += (bon*(score//10))

		return score

	def verificationPlateau(self, pose_choix):
		self.compteur_partie += 1
		rand = random.randint(1,2)

		bon = 0
		mauvais = 0

		for pose_joueur in pose_choix:
			if self.plateau_ref[pose_joueur[0]][pose_joueur[1]] == 3:
				self.plateau_jeu[pose_joueur[0]][pose_joueur[1]] = 6
				bon += 1
			else:
				self.win = False
				self.plateau_jeu[pose_joueur[0]][pose_joueur[1]] = 7
				mauvais += 1

		if bon == self.nb_atomes:
			if rand == 1:
				partWin1()

			elif rand == 2:
				partWin2()

		elif bon == 0:

			if rand == 1:
				partLose1()

			elif rand == 2:
				partLose2()

		return bon, mauvais