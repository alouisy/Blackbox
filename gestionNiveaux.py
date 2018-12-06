import os, copy
from affichage import *

def sauvegardeNiveau(taille, pose_atomes):

	if os.path.isdir("Niveaux") == False:
		os.mkdir("Niveaux")

	repertoirNiveaux = os.listdir("Niveaux")
	numNiveau = len(repertoirNiveaux)+1
	nom_niveau = "Niveaux/niveau_"+str(numNiveau)+".txt"
	Fniveau = open(nom_niveau, 'w')

	Fniveau.write(str(taille))
	Fniveau.write('\n')
	Fniveau.write(str(copy.deepcopy(pose_atomes)))
	Fniveau.write('\n')

	Fniveau.close()


def chargerNiveau(num_sauvegarde):

	if os.path.isdir("Niveaux") == True:
		tampon = []
		plateau = []

		try:
			nom_niveau = "Niveaux/niveau_"+num_sauvegarde+".txt"
			Fniveau = open(nom_niveau, 'r')
		except FileNotFoundError:
			nom_niveau = "Niveaux/niveau_"+str(1)+".txt"
			Fniveau = open(nom_niveau, 'r')

		taille = Fniveau.readline()
		taille = taille[:-1]
		taille = int(taille)

		tab_atomes = Fniveau.readline()
		tab_atomes = tab_atomes[:-1]
		tab_atomes = eval(tab_atomes)

	else:
		plateau = []

	return taille, tab_atomes


def editeurNiveau(fond, joueur, tab_plateau):
	erreur = True
	msg_erreur = ""
	taille_tab = 0

	while erreur == True:
		erreur = False

		try:
			taille_tab = int(recup_saisie("Entrez la taille du tableau", msg_erreur))
			msg_erreur = ""
		except ValueError:
			erreur = True
			msg_erreur = "Entrée invalide"

		else:
			if taille_tab < 5:
				erreur = True
				msg_erreur = "La taille du tableau doit être supérieur à 4"

	tab_plateau.creaTab(taille_tab)
	tab_plateau.set_joueur(joueur)
	
	LARGEUR = (len(tab_plateau.plateau_jeu)*(2+tab_plateau.taille_carreau))+(tab_plateau.taille_carreau*4)
	HAUTEUR = (len(tab_plateau.plateau_jeu)*(2+tab_plateau.taille_carreau))+(tab_plateau.taille_carreau*6)
	
	fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
	pygame.display.set_caption("Positionnement des atomes")
	initPlateau(2, tab_plateau)

	fenetre.fill(fond.fond_partie)
	
	font = pygame.font.Font(None, 24)
	font_2 = pygame.font.Font(None, 32)

	terminer_t = font_2.render("Terminer", 1, (100, 0, 100))
	
	while True:
		afficheTableau(fond.fond_partie, tab_plateau.plateau_ref, fenetre, tab_plateau.taille_carreau)
		sauvegarde = fenetre.blit(font_2.render("Sauvegarder la config", 1, (100, 0, 255)), (20, 10))
		restaure = fenetre.blit(font_2.render("Restaurer une config", 1, (100, 0, 255)), (20, 50))
		terminer = fenetre.blit(terminer_t, ((fenetre.get_width()//2)-(terminer_t.get_width()//2), fenetre.get_height()-50))

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == MOUSEBUTTONDOWN:
				
				if event.pos[0] > tab_plateau.plateau_pose[0][1].x and event.pos[0] < tab_plateau.plateau_pose[0][len(tab_plateau.plateau_ref)-2].x+tab_plateau.taille_carreau and event.pos[1] > tab_plateau.plateau_pose[1][0].y and event.pos[1] < tab_plateau.plateau_pose[len(tab_plateau.plateau_ref)-1][2].y:
					for i, ligne in enumerate(tab_plateau.plateau_pose):
						for j, poses in enumerate(ligne):
							if poses != 0:
								if event.pos[0] > poses.x and event.pos[0] < poses.x+poses.w and event.pos[1] > poses.y and event.pos[1] < poses.y+poses.h:
									if event.button == 1:

										if tab_plateau.plateau_ref[i][j] == 2:
											tab_plateau.plateau_ref[i][j] = 3
											tab_plateau.plateau_jeu[i][j] = 3

										elif tab_plateau.plateau_ref[i][j] == 3:
											tab_plateau.plateau_ref[i][j] = 2
											tab_plateau.plateau_jeu[i][j] = 2
				
				if event.pos[0] > sauvegarde.x and event.pos[0] < sauvegarde.x+sauvegarde.w and event.pos[1] > sauvegarde.y and event.pos[1] < sauvegarde.y+sauvegarde.h:
					print("sauvegarde")
					sauvegardeNiveau(tab_plateau.nb_cases, tab_plateau.tab_atomes)
					afficheTexte("La partie a bien été sauvegardée")
					fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
					
				elif event.pos[0] > restaure.x and event.pos[0] < restaure.x+restaure.w and event.pos[1] > restaure.y and event.pos[1] < restaure.y+restaure.h:
					print("Restaurer")
					tab_plateau.clear()
					tab_plateau = Plateau()
					nom_sauvegarde = recup_saisie("Entrez le numéros de la sauvegarde", msg_erreur)
					tab_plateau.nb_cases, tab_plateau.tab_atomes = chargerNiveau(nom_sauvegarde)
					tab_plateau.creaTab(tab_plateau.nb_cases-2)
					# tab_plateau.placeAtomes()
					initPlateau(2, tab_plateau)

				elif event.pos[0] > terminer.x and event.pos[0] < terminer.x+terminer.w and event.pos[1] > terminer.y and event.pos[1] < terminer.y+terminer.h:
					print("terminer")
					initPlateau(2, tab_plateau)
					return tab_plateau
		pygame.display.update()


def creationNiveau(niveau, tab_plateau):
	if niveau == 1:
		tab_plateau.creaTab(6)
		tab_plateau.nb_atomes = 3
	elif niveau == 2:
		tab_plateau.creaTab(9)
		tab_plateau.nb_atomes = 3
	elif niveau == 3:
		tab_plateau.creaTab(12)
		tab_plateau.nb_atomes = 5
	elif niveau == 4:
		tab_plateau.creaTab(15)
		tab_plateau.nb_atomes = 7
	elif niveau == 5:
		tab_plateau.creaTab(18)
		tab_plateau.nb_atomes = 7
	elif niveau == 6:
		tab_plateau.creaTab(21)
		tab_plateau.nb_atomes = 10
	tab_plateau.atomesAlea()
	initPlateau(2, tab_plateau)
	return tab_plateau