import pygame, sys, copy
from pygame.locals import *
from plateauJeu import *
from plateau import *


def initPlateau(op, plateau = None):

	if op == 0:
		tailleTab = int(recup_saisie("Entrer la taille du tableau"))
		tab_plateau = Plateau(tailleTab)
	elif op == 1:
		tab_plateau = plateau(len(plateau)-2)
		tab_plateau.copy_plateau(plateau)
	tab_plateau = plateau

	LARGEUR = (len(tab_plateau.plateau_jeu)*(2+tab_plateau.taille_carreau))+(tab_plateau.taille_carreau*4)
	HAUTEUR = (len(tab_plateau.plateau_jeu)*(2+tab_plateau.taille_carreau))+(tab_plateau.taille_carreau*6)

	x = 0
	y = tab_plateau.taille_carreau*3
	tabPosePlateau = [[0]*(len(tab_plateau.plateau_jeu)) for i in range(len(tab_plateau.plateau_jeu))]
	tabCarreauNoir = []
	tabAtomes = []

	fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
	pygame.display.set_caption('Black Box')
	tab_plateau.nb_atomes = 0

	for i, ranges in enumerate(tab_plateau.plateau_jeu):
		x = tab_plateau.taille_carreau
		for j, cases in enumerate(ranges):
			x += tab_plateau.taille_carreau+2
			if cases != 0:
				if cases == 1:
					tab_plateau.plateau_pose[i][j] = (pygame.draw.rect(fenetre, (255, 0, 0), (x, y, tab_plateau.taille_carreau, tab_plateau.taille_carreau)))
				elif cases != 1:
					tab_plateau.plateau_pose[i][j] = (pygame.draw.rect(fenetre, (0, 0, 0), (x, y, tab_plateau.taille_carreau, tab_plateau.taille_carreau)))
					if cases == 3:
						pygame.draw.circle(fenetre, (0, 255, 255), (x+15, y+15), 10)
						tab_plateau.tab_atomes.append((i, j))
						tab_plateau.nb_atomes += 1
		y += tab_plateau.taille_carreau+2

	tab_plateau.fenetre = fenetre
	
	bordAtomes(tab_plateau.plateau_jeu)
	bordAtomes(tab_plateau.plateau_ref)

	return tab_plateau



def afficheTableau(fond, plateau, fenetre, taille_carreau):

	fenetre.fill(fond)

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
				elif plateau[i][j] == 3:
					pygame.draw.circle(fenetre, (0, 255, 255), (x+15, y+15), 10)

		y += taille_carreau+2


def affichePlateau(plateau, fenetre, taille_carreau):

	x = 0
	y = taille_carreau*2

	for i, ranges in enumerate(plateau):
		x = taille_carreau
		for j, cases in enumerate(ranges):

			x += taille_carreau+2
			if cases == 1:
				pygame.draw.rect(fenetre, (255, 0, 0), (x, y, taille_carreau, taille_carreau))
			elif cases == 2:
				pygame.draw.rect(fenetre, (0, 0, 0), (x, y, taille_carreau, taille_carreau))
			elif cases == 3:
				pygame.draw.circle(fenetre, (0, 255, 255), (x+15, y+15), 10)
			elif cases == 4:
				pygame.draw.rect(fenetre, (0, 255, 0), (x, y, taille_carreau, taille_carreau))
			elif cases == 5:
				pygame.draw.rect(fenetre, (255, 255, 255), (x, y, taille_carreau, taille_carreau))
			elif cases == 6:
				pygame.draw.line(fenetre, (255, 255, 0), (x, y+15), (x+30, y+15), 5)
			elif cases == 7:
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y), (x+15, y+30), 5)
			elif cases == 11:
				pygame.draw.line(fenetre, (255, 255, 0), (x, y+15), (x+15, y+15), 5)
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y), (x+15, y+15), 5)
			elif cases == 12:
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y+15), (x+30, y+15), 5)
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y), (x+15, y+15), 5)
			elif cases == 13:
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y+15), (x+30, y+15), 5)
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y+15), (x+15, y+30), 5)
			elif cases == 14:
				pygame.draw.line(fenetre, (255, 255, 0), (x, y+15), (x+15, y+15), 5)
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y+15), (x+15, y+30), 5)
			elif cases == 14:
				pygame.draw.line(fenetre, (255, 255, 0), (x, y+15), (x+15, y+15), 5)
				pygame.draw.line(fenetre, (255, 255, 0), (x+15, y+15), (x+15, y+30), 5)

		y += taille_carreau+2

	pygame.display.update()


def recup_saisie(texte, erreur = "", titre_fenetre = "Saisie", taille_texte = 24):
	
	fpsClock = pygame.time.Clock()

	font = pygame.font.Font(None, taille_texte)
	
	texte = font.render(texte, 1, (255, 255, 255))
	erreur = font.render(erreur, 1, (255, 0, 0))
	
	if texte.get_width() > erreur.get_width():
		LARGEUR = texte.get_width()+50
	else:
		LARGEUR = erreur.get_width()+50

	HAUTEUR = 200
	fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
	pygame.display.set_caption(titre_fenetre)
	
	p_texte = fenetre.blit(texte, (10, 10))
	p_terminer = fenetre.blit(font.render("Terminer", 1, (0, 0, 255)), (LARGEUR-80, HAUTEUR-30))
	fenetre.blit(erreur, (5, HAUTEUR//2+20))
	saisie = ""
        	
	while True:
                
		zone_saisie = pygame.draw.rect(fenetre, (50, 50, 50), (0, p_texte.y+50, LARGEUR,p_texte.h))
		a_saisie = font.render(saisie, 1, (255, 255, 255))
		fenetre.blit(a_saisie, (LARGEUR//2-a_saisie.get_width()//2, zone_saisie.y))

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.pos[0] > p_terminer.x and event.pos[0] < p_terminer.x+p_terminer.w and event.pos[1] > p_terminer.y and event.pos[1] < p_terminer.y+p_terminer.h:
					return saisie
			elif event.type == KEYDOWN:
				if event.key == K_BACKSPACE:
					saisie = saisie[:-1]
				elif event.key == K_RETURN:
					return saisie
				else:
					saisie += event.unicode

				if a_saisie.get_width() >= LARGEUR:
					saisie = saisie[:-1]

		pygame.display.update()
		fpsClock.tick(10)


def afficheTexte(texte):

	fpsClock = pygame.time.Clock()

	font = pygame.font.Font(None, 32)
	
	tab_char = list(texte)
	max_char = 400
	maxi = 0
	div = 0

	texte = ""
	tab_texte = []
	max_largeur = 0
	maxi = 0
	tampon = ""

	print(tab_char)

	for charac in tab_char:
		if (charac == ' ' or charac == '/') and maxi >= max_char:
			tab_texte.append(texte)
			tampon = ""
			
		else:
			tampon += charac

			texte = font.render(tampon, 1, (255, 255, 255))
			maxi = texte.get_width()

			if maxi > max_largeur:
				max_largeur = maxi

	tab_texte.append(texte)
	
	LARGEUR = max_largeur+200 
	HAUTEUR = 300+(div*tab_texte[0].get_height())

	fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
	pygame.display.set_caption("Information")
	
	for i, texte in enumerate(tab_texte):
		p = fenetre.blit(texte, ((LARGEUR//2)-(texte.get_width()//2), (50+(50*i))))
		print(p)

	terminer = font.render("OK", 1, (0, 0, 255))

	p_terminer = fenetre.blit(terminer, ((LARGEUR//2)-(terminer.get_width()//2), p.y+60))
        	
	while True:

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == MOUSEBUTTONDOWN:
				if event.pos[0] > p_terminer.x and event.pos[0] < p_terminer.x+p_terminer.w and event.pos[1] > p_terminer.y and event.pos[1] < p_terminer.y+p_terminer.h:
					return

		pygame.display.update()
		fpsClock.tick(10)