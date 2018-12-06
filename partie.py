import socket, sys, pygame, threading
from pygame.locals import *
from affichage import *
from plateau import *
from joueur import *
from background import *
from parametre import *
from laser import *
from sounds import *
from serveurTchat import *
from clientTchat import *


#----------------------------------------------------------------MENU---------------------------------------------------------------------------------------
def menu(fond):
	LARGEUR = 640
	HAUTEUR = 480

	fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
	pygame.display.set_caption("Menu BlackBox")

	font = pygame.font.Font(None, 48)

	tab_menu = []
	options = font.render("Partie Solo", 1, (0, 0, 0))
	tab_menu.append((options, fenetre.blit(options, (LARGEUR//2-options.get_width()//2, HAUTEUR//2-options.get_height()//2))))

	options = font.render("Partie Multi", 1, (0, 0, 0))
	tab_menu.append((options, fenetre.blit(options, (LARGEUR//2-options.get_width()//2, HAUTEUR//2-options.get_height()//2))))

	options = font.render("Options", 1, (0, 0, 0))
	tab_menu.append((options, fenetre.blit(options, (LARGEUR//2-options.get_width()//2, HAUTEUR//2-options.get_height()//2))))

	options = font.render("Aide", 1, (0, 0, 0))
	tab_menu.append((options, fenetre.blit(options, (LARGEUR//2-options.get_width()//2, HAUTEUR//2-options.get_height()//2))))


	x = tab_menu[1][1].x-100
	x1 = tab_menu[1][1].x+tab_menu[1][1].w+100
	y = tab_menu[1][1].y+tab_menu[1][1].h//2
	taille_triangle = 30
	tab_menu.append((pygame.draw.polygon(fenetre, (255, 255, 255), ((x, y), (x+taille_triangle, y-taille_triangle), (x+taille_triangle, y+10))),
	pygame.draw.polygon(fenetre, (255, 255, 255), ((x1, y), (x1-taille_triangle, y-taille_triangle), (x1-taille_triangle, y+taille_triangle)))))

	fenetre.fill(fond.fond_partie)
	fenetre.blit(tab_menu[0][0], (tab_menu[0][1].x, tab_menu[0][1].y))

	i = 0
	
	afficheMenu(fenetre, tab_menu, i)
    
	clic = False

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				clic = True
			elif event.type == MOUSEBUTTONUP:
				clic = False

			if clic == True or event.type == MOUSEMOTION:
				if event.pos[0] > tab_menu[i][1].x and event.pos[0] < tab_menu[i][1].x+tab_menu[i][1].w and event.pos[1] > tab_menu[i][1].y and event.pos[1] < tab_menu[i][1].y+tab_menu[i][1].h:
					if clic == True:#Lancer la partie SOLO
						if i == 0:
							return 2
						elif i == 1:#Lancer la partie MULTI
							return 4
						elif i == 2:#Réglages
							return 3
						elif i == 3:#Aide
							os.system("start web/regles/regles.html")
					else:
						pygame.draw.rect(fenetre, (255, 255, 255), tab_menu[i][1])
						afficheMenu(fenetre, tab_menu, i)
				else:
					fenetre.fill(fond.fond_partie)
					afficheMenu(fenetre, tab_menu, i)
				
				if clic == True:
					if event.pos[0] > tab_menu[len(tab_menu)-1][0].x and event.pos[0] < tab_menu[len(tab_menu)-1][0].x+tab_menu[len(tab_menu)-1][0].w and event.pos[1] > tab_menu[len(tab_menu)-1][0].y and event.pos[1] < tab_menu[len(tab_menu)-1][0].y+tab_menu[len(tab_menu)-1][0].h:#Flèche de gauche
						i = animation_menu(fond, fenetre, tab_menu, i, 0)
					elif event.pos[0] > tab_menu[len(tab_menu)-1][1].x and event.pos[0] < tab_menu[len(tab_menu)-1][1].x+tab_menu[len(tab_menu)-1][1].w and event.pos[1] > tab_menu[len(tab_menu)-1][1].y and event.pos[1] < tab_menu[len(tab_menu)-1][1].y+tab_menu[len(tab_menu)-1][1].h:#Flèche de droite
						i = animation_menu(fond, fenetre, tab_menu, i, 1)


def afficheMenu(fenetre, tab_menu, i, x_text = 0, y_text = 0):
		
		x = tab_menu[1][1].x-100
		y = tab_menu[1][1].y+tab_menu[1][1].h//2
		taille_triangle = 30
		pygame.draw.polygon(fenetre, (255, 255, 255), ((x, y), (x+taille_triangle, y-taille_triangle), (x+taille_triangle, y+taille_triangle)))
		x = tab_menu[1][1].x+tab_menu[1][1].w+100
		pygame.draw.polygon(fenetre, (255, 255, 255), ((x, y), (x-taille_triangle, y-taille_triangle), (x-taille_triangle, y+taille_triangle)))
		if x_text == 0 and x_text == 0:
			x_text = tab_menu[i][1].x
			y_text = tab_menu[i][1].y
		fenetre.blit(tab_menu[i][0], (x_text, y_text))
		pygame.display.update()


#----------------------------------------------------------------ANIMATION DU MENU---------------------------------------------------------------------------------------
def animation_menu(fond, fenetre, tab_menu, i, op):
	if i > len(tab_menu)-2:
		i = 0
	x = 0

	fps = pygame.time.Clock()
	
	option = fenetre.blit(tab_menu[i][0], (tab_menu[i][1].x, tab_menu[i][1].y))
	x1 = option.x
	for tour in range(2):
		if op == 1:
			x1 = option.x
			while x1 < option.x+fenetre.get_width()//2-option.w//2:
				x+=1
				x1 += x
				fenetre.fill(fond.fond_partie)
				afficheMenu(fenetre, tab_menu, i, x1, option.y)
				fps.tick(100)
			if tour == 1:
				continue
			i+=1
			if i > len(tab_menu)-2:
				i = 0
			x = 0
			option = fenetre.blit(tab_menu[i][0], (0, tab_menu[i][1].y))
	if op == 0:
		while x1 > 0:
			x+=1
			x1 -= x
			fenetre.fill(fond.fond_partie)
			afficheMenu(fenetre, tab_menu, i, x1, option.y)
			fps.tick(100)

		i-=1
		if i < 0:
			i = len(tab_menu)-2
		x = 0
		option = fenetre.blit(tab_menu[i][0], (0, tab_menu[i][1].y))
		x1 = fenetre.get_width()
		while x1 > option.x+(fenetre.get_width()//2-option.w//2):
			x-=1
			x1 += x
			fenetre.fill(fond.fond_partie)
			afficheMenu(fenetre, tab_menu, i, x1, option.y)
			fps.tick(100)
			
	fenetre.fill(fond.fond_partie)
	fenetre.blit(tab_menu[i][0], (tab_menu[i][1].x, tab_menu[i][1].y))
	afficheMenu(fenetre, tab_menu, i)
	pygame.display.update()
	return i


#----------------------------------------------------------------CLASSE PARTIE---------------------------------------------------------------------------------------
class Jeu:
	LARGEUR = 0
	HAUTEUR = 0
	fenetre = None
	vu_souris = False
	fond = None
	hote = ''
	port = 1024
	mode_mutli = False
	mode_server = False
	
	coups = 0
	partie_termine = False

	def __init__(self, fond, joueur, tab_plateau, son):
		self.fond = fond
		self.tab_plateau = tab_plateau
		self.joueur = joueur
		self.laser = Laser()
		self.son = son
		

	def initFenetre(self):
		self.LARGEUR = (self.tab_plateau.nb_cases*(2+self.tab_plateau.taille_carreau))+(self.tab_plateau.taille_carreau*4)+300
		self.HAUTEUR = (self.tab_plateau.nb_cases*(2+self.tab_plateau.taille_carreau))+(self.tab_plateau.taille_carreau*6)
		self.fenetre = pygame.display.set_mode((self.LARGEUR, self.HAUTEUR))
		pygame.display.set_caption("BlackBox")
		self.fenetre.fill(self.fond.fond_partie)


	#----------------------------------------------------------------------------SOLO-------------------------------------------------------------------------------
	def partieSolo(self):
		stop = False
		pause = False
		choix = 8
		self.val_retour = False

		while not stop:
			if choix == 9:
				self.val_retour = True
				choix = gestionParametres(self.fond, self.son, True)
				if choix == 0:
					choix = 7
				if choix == 1:
					return choix
				elif choix == 2:
					choix = 8

			if choix == 8:
				self.tab_plateau, self.joueur, self.laser, choix = choixNiveau(self.fond, self.tab_plateau, self.joueur, self.laser, self.val_retour)
				if choix == 0:
					choix = 9
				elif choix == 1:
					self.initFenetre()
					self.coups = 0
					choix = 7
					
			if choix == 7:
				pause = False
				self.partie_termine = False
				self.initFenetre()

				self.son.playSong(1)

				self.tab_plateau.set_joueur(self.joueur)
				self.joueur.essais = self.tab_plateau.nb_atomes

				end = True
				
				interactions = []
				font = pygame.font.Font(None, 24)
				font_2 = pygame.font.Font(None, 48)

				options = pygame.draw.rect(self.fenetre, (0, 0, 0), (self.tab_plateau.plateau_pose[1][self.tab_plateau.nb_cases-1].x+(self.tab_plateau.taille_carreau*3), self.tab_plateau.taille_carreau*2, 250, self.HAUTEUR-(self.tab_plateau.taille_carreau*4)))
				nom = font_2.render(self.joueur.nom, 1, (0, 255, 0))
				coups_partie = font_2.render(str(self.coups), 1, (50, 50, 255))

				interactions.append(self.fenetre.blit(nom, (options.x+((options.w//2)-(nom.get_width()//2)), options.y+60)))
				interactions.append(self.fenetre.blit(pygame.image.load("Images/reglage.png"), (self.fenetre.get_width()-50, 10)))

				sourisX = 0
				sourisY = 0
				clic = 0

				while not pause:

					retour, clic = self.interactionsPartie(sourisX, sourisY, clic, interactions)
					if self.joueur.essais == 0 and end == True:
						end = False
						self.partie_termine = True
						self.son.stopAllSong()
						self.tab_plateau.gestionScore(self.joueur.pose_choix)
						
						self.tab_plateau.vu_atomes = True
						self.initFenetre()

					if retour == "break":
						choix = clic
						pause = True
						self.val_retour = False
						continue
					elif retour == "break_2":
						choix = clic
						pause = True
						stop = True
						continue

					self.fenetre.fill(self.fond.fond_partie)

					nom = font_2.render(self.joueur.nom, 1, (0, 255, 0))
					options = pygame.draw.rect(self.fenetre, (0, 0, 0), (self.tab_plateau.plateau_pose[1][self.tab_plateau.nb_cases-1].x+(self.tab_plateau.taille_carreau*3), self.tab_plateau.taille_carreau*2, 250, self.HAUTEUR-(self.tab_plateau.taille_carreau*4)))
					coups_partie = font_2.render(str(self.coups), 1, (50, 50, 255))
					nb_essais = font_2.render("%d essais" % self.joueur.essais, 1, (150, 0, 200))

					self.fenetre.blit(font_2.render("Joueur :", 1, (255, 255, 255)), (options.x+5, options.y+5))
					self.fenetre.blit(nom, (options.x+((options.w//2)-(nom.get_width()//2)), options.y+60))
					self.fenetre.blit(font_2.render("Coups :", 1, (255, 255, 255)), (options.x+5, options.y+140))
					self.fenetre.blit(coups_partie, (options.x+((options.w//2)-(coups_partie.get_width()//2)), options.y+180))
					self.fenetre.blit(nb_essais, (options.x+((options.w//2)-(nb_essais.get_width()//2)), options.y+220))

					self.fenetre.blit(pygame.image.load("Images/reglage.png"), (self.fenetre.get_width()-50, 10))

					self.tab_plateau.afficheTableau(self.tab_plateau.plateau_ref, self.fenetre, self.tab_plateau.taille_carreau)
					gestionLaser(self.tab_plateau, self.laser, clic)

					self.afficheTexte()

					self.tab_plateau.affiche_clic()
					self.poseSouris(sourisX, sourisY)
					if self.vu_souris == True:
						self.suivreSouris(sourisX, sourisY, clic)


					pygame.display.update()
					sourisX, sourisY, clic = self.joueur.coordonnees()#clic permet de savoir qu'elle touche de la souris a été utilisé

		return 1


	def afficheTexte(self):#Affichage du nombre d'atome et des interractions des lasers
		font = pygame.font.Font(None, 32)

		texte_haut = font.render("%d atomes à trouver" % self.tab_plateau.nb_atomes, 1, (150, 0, 200))
		texte_bas = font.render(self.laser.texte_laser, 1, (0, 0, 0))

		self.fenetre.blit(texte_haut, (((self.LARGEUR//2)-texte_haut.get_width()//2), self.tab_plateau.taille_carreau))
		self.fenetre.blit(texte_bas, (((self.LARGEUR//2)-texte_bas.get_width()//2), self.HAUTEUR-(self.tab_plateau.taille_carreau*2)))


	def interactionsPartie(self, sourisX, sourisY, clic, interactions):#Permet de gérer les différentes options de la partie

		if self.partie_termine == False:#Tant que la partie n'est pas terminé
			for i, ligne in enumerate(self.tab_plateau.plateau_pose):#Parcours le tableau des positions pour trouver l'emplacement du pointeur sur le plateau de jeu
				for j, val in enumerate(ligne):
					if val != 0:
						if sourisX > val.x and sourisX < val.x+val.w and sourisY > val.y and sourisY < val.y+val.h:
							if clic == 1:
								if self.tab_plateau.plateau_jeu[i][j] == 1:#Les cases rouge
									self.son.playSongClic()
									clic = 255
									self.joueur.poses_clic.append((i, j))
									self.coups += 1
									self.tab_plateau.compteur_coups += 1
									if i == 0:
										self.tab_plateau.plateau_jeu[i][j] = 4
										self.laser.set_coord((j, i, 1))

									elif i == (len(self.tab_plateau.plateau_jeu)-1):
										self.tab_plateau.plateau_jeu[i][j] = 4
										self.laser.set_coord((j, i, 2))

									elif j == 0:
										self.tab_plateau.plateau_jeu[i][j] = 4
										self.laser.set_coord((j, i, 3))

									elif j == (len(self.tab_plateau.plateau_jeu)-1):
										self.tab_plateau.plateau_jeu[i][j] = 4
										self.laser.set_coord((j, i, 4))

								elif self.tab_plateau.plateau_ref[i][j] != 1 and self.joueur.essais > 0 and self.tab_plateau.plateau_jeu[i][j] != 8:#Les cases noir
									self.joueur.essais -= 1
									self.joueur.poses_clic.append((i, j))
									self.joueur.pose_choix.append([i, j])
									self.tab_plateau.plateau_jeu[i][j] = 8

			if clic == 1:
				for i, zone in enumerate(interactions):

					if sourisX > zone.x and sourisX < zone.x+zone.w and sourisY > zone.y and sourisY < zone.y+zone.h:
						if i == 0 and self.mode_server == False:#Changer le pseudonyme
							erreur = ""
							teste_nom = True

							while teste_nom:
								teste_nom = False
								nom = recup_saisie("Changer de pseudo", erreur)
								if len(nom) > 13:
									teste_nom = True
									erreur = "Nom trop long"
								elif len(nom) == 0:
									teste_nom = True
									erreur = "Nom trop court"
							
							self.initFenetre()

							if nom[0] == "_":
								return self.cheat(nom)

							else:
								self.joueur.nom = nom
						
						elif i == 1 and self.mode_mutli == False:#Réglages du jeu
							return "break", 9

		elif self.partie_termine == True:#Si la partie est terminée
			font = pygame.font.Font(None, 48)

			termine_tab = []

			recommencer = font.render("Recommencer", 1, (255, 255, 255))
			quitter = font.render("Quitter", 1, (255, 255, 255))

			termine_tab.append(self.fenetre.blit(recommencer, ((self.LARGEUR//3)-(recommencer.get_width()//2), (self.HAUTEUR//2)-recommencer.get_height()//2)))
			termine_tab.append(self.fenetre.blit(quitter, ((self.LARGEUR//3)+((self.LARGEUR//3))-(quitter.get_width()//2), (self.HAUTEUR//2)-quitter.get_height()//2)))

			while True:
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()

					if event.type == MOUSEBUTTONDOWN:
						for i, inter in enumerate(termine_tab):
							if event.pos[0] >= inter.x and event.pos[0] < inter.x+inter.w and event.pos[1] >= inter.y and event.pos[1] < inter.y+inter.h:
								self.son.stopAllSong()
								if i == 0:#Refaire une partie
									return "break", 8
								elif i == 1:#Quitter le jeu
									return "break_2", 0

				pygame.display.update()

		return 0, clic


	def cheat(self, code):#Cheat code du jeu
		try:
			if code.upper() == "_SHOWATOMS_":#Montrer les atomes du jeu
				self.tab_plateau.vu_atomes = not self.tab_plateau.vu_atomes
			elif code.upper() == "_SHOWLASERS_":#Montrer les lasers du jeu
				self.tab_plateau.vu_laser = not self.tab_plateau.vu_laser
			elif code.upper() == "_REPLAY_":#Relancer la partie
				return "break", 8
			elif code.upper() == "_EXITGAME_":#Quitter la partie
				return "break_2", 9
			elif "_SCORECHANGE_" in code.upper():#Changer le score
				self.joueur.score = int(code[code.index(":")+1:])
			elif "_CHANGECOLOR_" in code.upper():#Changer la couleur de fond
				self.fond.fond_partie = eval(code[code.index(":")+1:])
			elif "_CHANGELEVEL_" in code.upper():#Chnger le niveau
				niveau = int(code[-1])

				self.joueur.clear()
				self.laser.clear()
				self.tab_plateau.clear()

				self.joueur = Joueur()
				self.laser = Laser()
				self.tab_plateau = Plateau()
				self.tab_plateau = creationNiveau(niveau, self.tab_plateau)
		except:
			pass
		return 0, 255


	def poseSouris(self, sourisX, sourisY):#Surligne la case où se trouve le pointeur de la souris
		if self.partie_termine == False:
			for i, ligne in enumerate(self.tab_plateau.plateau_pose):
				for j, val in enumerate(ligne):
					if val != 0:
						if sourisX > val.x and sourisX < val.x+val.w and sourisY > val.y and sourisY < val.y+val.h:
							pygame.draw.rect(self.fenetre, (0, 255, 255), (self.tab_plateau.plateau_pose[i][j].x, self.tab_plateau.plateau_pose[i][j].y, self.tab_plateau.taille_carreau, self.tab_plateau.taille_carreau))


	def suivreSouris(self, sourisX, sourisY, clic):#Permet d'afficher un pointeur à l'emplacement du pointeur du joueur en mode MULTI
		souris_1 = pygame.image.load("Images/souris.png")

		self.fenetre.blit(souris_1, (sourisX, sourisY))


#----------------------------------------------------------------------------MULTI-------------------------------------------------------------------------------
	def gestionMulti(self):#Permet au joueur de choisir entre héberger et rejoindre une partie
		LARGEUR = 500
		HAUTEUR = 350

		fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

		fenetre.fill(self.fond.fond_partie)

		self.mode_mutli = True

		font = pygame.font.Font(None, 48)
		titre = font.render("Choix de la partie", 1, (255, 0, 255))
		heberge = font.render("Héberger la partie", 1, (0, 0, 255))
		rejoindre = font.render("Rejoindre partie", 1, (0, 0, 255))

		fenetre.blit(titre, ((LARGEUR//2)-(titre.get_width()//2), 10))
		heberge_p = fenetre.blit(heberge, ((LARGEUR//2)-(heberge.get_width()//2), 150))
		rejoindre_p = fenetre.blit(rejoindre, ((LARGEUR//2)-(rejoindre.get_width()//2), heberge_p.y+80))

		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			if event.type == MOUSEBUTTONDOWN:
				if event.pos[0] >= heberge_p.x and event.pos[0] < heberge_p.x+heberge_p.w and event.pos[1] >= heberge_p.y and event.pos[1] < heberge_p.y+heberge_p.h:#Héberger
					self.mode_server = True
					return 

				elif event.pos[0] >= rejoindre_p.x and event.pos[0] < rejoindre_p.x+rejoindre_p.w and event.pos[1] >= rejoindre_p.y and event.pos[1] < rejoindre_p.y+heberge_p.h:#Rejoindre
					self.mode_server = False
					return
			
			pygame.display.update()


	def waitGamer(self):#Affiche un message d'attente pour le joueur qui héberge la partie en attendant une connection d'un joueur
		font = pygame.font.Font(None, 48)

		texte = font.render("En attente d'un joueur...", 1, (0, 100, 100))

		self.fenetre.blit(texte, ((self.LARGEUR//2)-(texte.get_width()//2), (self.HAUTEUR//2)-(texte.get_height()//2)))

		pygame.display.update()


	def partieMulti(self):
		stop = False
		pause = False

		while not stop:
			self.coups = 0
			start_tchat = False
			self.gestionMulti()
			pause = False
			self.partie_termine = False
			self.son.playSong(1)

			laser = Laser()

			if self.mode_server == True:
				serveurMulti = Server()
				serveurMulti.start()
				serveurMulti.setJoueur(self.joueur)

				editeurNiveau(self.fond, self.joueur, self.tab_plateau)

				self.tab_plateau.vu_atomes = True
				self.tab_plateau.vu_laser = True
				self.vu_souris = True

				config = (self.tab_plateau.taille_carreau,
						self.tab_plateau.taille_atome,
						self.tab_plateau.taille_laser,
						self.tab_plateau.nb_atomes,
						self.tab_plateau.nb_cases-2)

				serveurMulti.setConfig(self.tab_plateau.tab_atomes, config)
				t1 = 0
				self.initFenetre()
				self.waitGamer()
			else:
				clientMulti = Client()
				clientMulti.start()
				clientMulti.nom_hote = recup_saisie("Entrez l'adresse de l'hote", clientMulti.msg_err)
				self.tab_plateau.set_joueur(self.joueur)

				while clientMulti.msg_get != "EC":
					pass

				clientMulti.sendName(self.joueur.nom)
				self.tab_plateau.taille_carreau = clientMulti.tab_config[0]
				self.tab_plateau.taille_atome = clientMulti.tab_config[1]
				self.tab_plateau.taille_laser = clientMulti.tab_config[2]
				self.tab_plateau.nb_atomes = clientMulti.tab_config[3]
				self.tab_plateau.nb_cases = clientMulti.tab_config[4]

				self.tab_plateau.creaTab(self.tab_plateau.nb_cases)


				for i in range(0, len(clientMulti.tab_atomes), 2):
					self.tab_plateau.plateau_ref[clientMulti.tab_atomes[i]][clientMulti.tab_atomes[i+1]] = 3
					self.tab_plateau.plateau_jeu[clientMulti.tab_atomes[i]][clientMulti.tab_atomes[i+1]] = 3
				
				initPlateau(2, self.tab_plateau)
				self.tab_plateau.vu_atomes = False
				self.tab_plateau.vu_laser = False
				self.vu_souris = False
				self.initFenetre()
				
				nom_joueur = self.joueur.nom
				clientMulti.sendName(self.joueur.nom)

			self.joueur.essais = self.tab_plateau.nb_atomes

			end = True
			
			interactions = []
			font = pygame.font.Font(None, 24)
			font_2 = pygame.font.Font(None, 48)


			options = pygame.draw.rect(self.fenetre, (0, 0, 0), (self.tab_plateau.plateau_pose[1][self.tab_plateau.nb_cases-1].x+(self.tab_plateau.taille_carreau*3), self.tab_plateau.taille_carreau*2, 250, self.HAUTEUR-(self.tab_plateau.taille_carreau*4)))
			nom = font_2.render(self.joueur.nom, 1, (0, 255, 0))
			coups_partie = font_2.render(str(self.coups), 1, (50, 50, 255))

			interactions.append(self.fenetre.blit(nom, (options.x+((options.w//2)-(nom.get_width()//2)), options.y+60)))
			f_tchat = font_2.render("Tchat", 1, (150, 50, 50))

			sourisX = 0
			sourisY = 0
			clic = 0

			
			while not pause:
				for event in pygame.event.get():
					if event.type == QUIT:
						if self.mode_server == True:
							serveurMulti.stop_serv = True
						else:
							clientMulti.stop_cli = True
						pygame.quit()
						sys.exit()

				if self.mode_server == True:
					if serveurMulti.move == "" and len(serveurMulti.tab_clic) == 0:
						continue

					if serveurMulti.erreur == True:
						break

					if len(serveurMulti.tab_clic) > 0:
						coord = serveurMulti.tab_clic.pop(0)
					else:
						coord = serveurMulti.move
						serveurMulti.move = ""
						
					try:
						sourisX = int(coord[1:coord.index('..')])
						sourisY = int(coord[coord.index('..')+2:coord.index('...')])
						clic = int(coord[coord.index('...')+3:])
					except ValueError:
						continue
					nom = font_2.render(serveurMulti.nom, 1, (0, 255, 0))
					t1+=1

				else:
					sourisX, sourisY, clic = self.joueur.coordonnees()
					if clic == 1:
						clientMulti.tab_clic.append("."+str(sourisX)+'..'+str(sourisY)+'...'+str(clic))
					elif clic == 0:
						clientMulti.move = "."+str(sourisX)+'..'+str(sourisY)+'...'+str(clic)

					if nom_joueur != self.joueur.nom:
						clientMulti.sendName(self.joueur.nom)
						nom_joueur = self.joueur.nom
						nom = font_2.render(self.joueur.nom, 1, (0, 255, 0))


				retour, clic = self.interactionsPartie(sourisX, sourisY, clic, interactions)
				if self.joueur.essais == 0 and end == True:
					end = False
					self.partie_termine = True
					self.son.stopAllSong()
					self.tab_plateau.gestionScore(self.joueur.pose_choix)
					self.initFenetre()

				if retour == "break":
					if self.mode_server == True:
						serveurMulti.stop_serv = True
					else:
						clientMulti.stop_cli = True
					pause = True
					return 4
					continue
				elif retour == "break_2":
					if self.mode_server == True:
						serveurMulti.stop_serv = True
					else:
						clientMulti.stop_cli = True
					pause = True
					stop = True
					return 1
					continue

				self.fenetre.fill(self.fond.fond_partie)

				options = pygame.draw.rect(self.fenetre, (0, 0, 0), (self.tab_plateau.plateau_pose[1][self.tab_plateau.nb_cases-1].x+(self.tab_plateau.taille_carreau*3), self.tab_plateau.taille_carreau*2, 250, self.HAUTEUR-(self.tab_plateau.taille_carreau*4)))
				coups_partie = font_2.render(str(self.coups), 1, (50, 50, 255))
				nb_essais = font_2.render("%d essais" % self.joueur.essais, 1, (150, 0, 200))

				self.fenetre.blit(font_2.render("Joueur :", 1, (255, 255, 255)), (options.x+5, options.y+5))
				self.fenetre.blit(nom, (options.x+((options.w//2)-(nom.get_width()//2)), options.y+60))
				self.fenetre.blit(font_2.render("Coups :", 1, (255, 255, 255)), (options.x+5, options.y+140))
				self.fenetre.blit(coups_partie, (options.x+((options.w//2)-(coups_partie.get_width()//2)), options.y+180))
				self.fenetre.blit(nb_essais, (options.x+((options.w//2)-(nb_essais.get_width()//2)), options.y+220))
				p_tchat = self.fenetre.blit(f_tchat, (options.x+((options.w//2)-(nb_essais.get_width()//2)), options.y+280))

				if sourisX >= p_tchat.x and sourisX < p_tchat.x+p_tchat.w and sourisY >= p_tchat.y and sourisY < p_tchat.y+p_tchat.h and clic == 1 and start_tchat == False:
					if self.mode_server == True:
						tchat_ser = servTchat()
						tchat_ser.start()
						start_tchat = True
					elif self.mode_server == False:
						tchat_cli = cliTchat()
						tchat_cli.setIp(clientMulti.nom_hote)
						tchat_cli.start()
						start_tchat = True

				self.tab_plateau.afficheTableau(self.tab_plateau.plateau_ref, self.fenetre, self.tab_plateau.taille_carreau)
				gestionLaser(self.tab_plateau, self.laser, clic)

				self.afficheTexte()

				self.tab_plateau.affiche_clic()
				self.poseSouris(sourisX, sourisY)
				if self.vu_souris == True:
					self.suivreSouris(sourisX, sourisY, clic)


				pygame.display.update()

			self.joueur.clear()
			self.laser.clear()
			self.tab_plateau.clear()

		return choix


class Server(threading.Thread):#Thread serveur
	hote = ''
	port = 1024
	msg_set = ""
	msg_get = "1"
	tab_options = []
	tab_coords = []
	tab_clic = []
	config = 1
	start_game = False
	move = ""
	nom = ""
	i = 0
	j = -1
	stop_serv = False
	erreur = False
	connecte = False

	def setJoueur(self, joueur):
		self.joueur = joueur

	def sendRcv(self, data):
		msg_envoye = data.encode()

		try:
			self.socket_cli.send(msg_envoye)
		except ConnectionResetError:
			self.erreur = True

		self.msg_set = ""

		message_recu = self.socket_cli.recv(1024)
		return message_recu.decode()


	def setConfig(self, tab_atomes, tab_config):
		self.tab_atomes = tab_atomes
		self.tab_config = tab_config


	def sendConfig(self):
		stop = False

		if self.config == 1:
			for coords in self.tab_atomes:
				for poseIJ in coords:
					self.sendRcv(str(poseIJ))

			self.config = 2
			self.sendRcv("EA")

		if self.config == 2:
			for param in self.tab_config:
				self.sendRcv(str(param))
			self.config = 3
			self.msg_get = self.sendRcv("EC")

	def getMove(self):

		if self.msg_get[len(self.msg_get)-1] == "1":
			self.tab_clic.append(self.msg_get)
		else:
			self.move = self.msg_get

		self.msg_set = "1"

		self.msg_get = ""

	def run(self):
		stop = False
		connecte = False
		erreur = ""

		while not stop:
			self.i = 0
			self.j = -1
			message = b""


			self.socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			self.socket_serv.bind((self.hote, self.port))

			self.socket_serv.listen(5)

			self.socket_cli, info_co = self.socket_serv.accept()
			msg_recu = b""

			message_recu = self.socket_cli.recv(1024)
			self.msg_get = message_recu.decode()

			self.erreur = False

			while not self.stop_serv:
				if self.msg_get != "":
					if self.msg_get == "1":
						self.sendConfig()

					elif self.msg_get[0] == ".":
						self.getMove()

					elif self.msg_get[0] == "+":
						self.nom = self.msg_get[1:]
						self.msg_get = self.sendRcv("ACK")

				if self.msg_set != "":
					self.msg_get = self.sendRcv(self.msg_set)
				
				if self.erreur == True:
					self.erreur = False
					stop = True

					for er in range(50):
						afficheTexte("Connexion interrompue")
					break

			if self.stop_serv == True:
				stop = True

		self.socket_cli.close()
		self.socket_serv.close()


class Client(threading.Thread):#Thread client
	nom_hote = ""
	port_hote = 1024
	msg_get = ""
	msg_set = "1"
	msg_config = ""
	tab_config = []
	tab_atomes = []
	tab_coords = []
	tab_clic = []
	config = 0
	nom = ""
	start_game = False
	move = ""
	stop_cli = False
	erreur = False
	connecte = False
	msg_err = ""


	def getConfig(self):
		stop = False
		atome = []
		self.config = 1
		j = 0
		i = 0

		self.msg_get = ""

		if self.config == 1:
			while not stop:#End Atoms
				data_get = self.sendRcv("1")

				if data_get == "EA":
					stop = True
					continue

				self.tab_atomes.append(int(data_get))

			self.config = 2
			stop = False
			data_get = ""

		if self.config == 2:
			while not stop:#End Config
				data_get = self.sendRcv("1")

				if data_get == "EC":
					stop = True
					continue

				self.tab_config.append(int(data_get))

		self.msg_get = data_get
		self.msg_set = ""


	def sendMove(self):
		stop = False
		self.msg_get = ""
		data_set = ""
		data_get = ""

		while not stop:
			if len(self.tab_clic) > 0:
				data_set = self.tab_clic.pop(0)
			elif len(self.move) != 0:
				data_set = self.move

			if data_set != "":
				data_get = self.sendRcv(data_set)

			if data_get != "3":
				stop = True
				self.msg_get = data_get

			if self.erreur == True:
				break

	def sendName(self, nom):

		self.msg_get = self.sendRcv("+"+nom)
		self.msg_get = "3"


	def sendRcv(self, data):
		
		msg_envoye = data.encode()

		try:
			self.socket_cli.send(msg_envoye)
		except ConnectionResetError:
			self.erreur = True

		message_recu = self.socket_cli.recv(1024)
		return message_recu.decode()


	def run(self):
		stop = False
		connecte = False

		while not stop:
			self.socket_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			try_connect = True
			self.msg_err = ""

			while try_connect == True:
				if self.nom_hote != "":
					try_connect = False
					try:
						self.socket_cli.connect((self.nom_hote, self.port_hote))
					except ConnectionRefusedError:
						try_connect = True
						self.msg_err = "Connexion impossible"
						self.nom_hote = ""
					
			connecte = True
			msg_envoye = b""

			self.getConfig()

			self.erreur = False


			while not self.stop_cli:
				if len(self.tab_clic) > 0 or self.move != "":
					self.sendMove()
				

				if self.msg_set != "" :

					if self.msg_set != "":
						self.msg_get = self.sendRcv(self.msg_set)

					if self.msg_get == "EC":
						self.start_game = True

					if self.msg_get == "error_404":
						break
					if self.erreur == True:
						self.erreur = False
						stop = True

						for er in range(50):
							afficheTexte("Connexion interrompue")

						break

				if self.stop_cli == True:
					stop = True


		self.socket_cli.close()