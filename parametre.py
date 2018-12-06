import pygame, sys
from pygame.locals import *
from sounds import *
from gestionNiveaux import *
from joueur import *
from laser import *

def gestionParametres(fond, son, game):
   LARGEUR = 600
   HAUTEUR = 400
   
   fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
   pygame.display.set_caption("Parametres")

   son.playSong(3)

   clic = False
   jouer_son = False
   x = 0
   test = False

   options = []


   while True:

      ligne_son, niveau_son, icon_volume, options = affichageParametre(fenetre, son, x, game)
      son.choixVolume(((niveau_son.x-ligne_son.x)/((ligne_son.x+ligne_son.w-5)-ligne_son.x))*100)

      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         if event.type == MOUSEBUTTONDOWN:
            clic = True
         elif event.type == MOUSEBUTTONUP:
            clic = False
            
            if jouer_son == True:
               jouer_son = False

         if clic == True:
            if event.pos[0] > ligne_son.x+1 and event.pos[0] < ligne_son.x+ligne_son.w-niveau_son.w//2 and event.pos[1] > icon_volume.y and event.pos[1] < icon_volume.y+icon_volume.h:
               x = event.pos[0]-niveau_son.w//2
               if event.type == MOUSEMOTION and event.pos[0] > ligne_son.x and event.pos[0] < ligne_son.x+ligne_son.w:
                     x = event.pos[0]-niveau_son.w//2
               jouer_son = True
            for index, option in enumerate(options):
               if event.pos[0] >= option.x and event.pos[0] < option.x+option.w and event.pos[1] >= option.y and event.pos[1] < option.y+option.h: 
                  if index == 1:
                     print("changer couleur fond")
                     fond.choixFond()

                  elif index == 2:
                     print("changer musique")
                     changerMusique(son)
                     son.playSong(3)

                  elif index == 3:
                     print("retour")
                     return 0

                  elif index == 4 and game == True:
                     print("menu")
                     return 1

                  elif index == 5 and game == True:
                     print("changer niveau")
                     return 2
                  
                  fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
                  pygame.display.set_caption("Parametres")

      if test == True:
         pygame.draw.rect(fenetre, (255, 255, 255), (p_partie.x+p_partie.w+10, p_partie.y+p_partie.h-20, 100, 250))
      pygame.display.update()

def affichageParametre(fenetre, son, x, game):
      LARGEUR = 600
      HAUTEUR = 400
      w = 200
      h = 50
      font_1 = pygame.font.Font(None, 48)
      font = pygame.font.Font(None, 24)

      options = []
      id_tab = 0
   
      fenetre.fill((150, 150, 150))
      fenetre.blit(font_1.render("PARAMETRES", 1, (0, 255, 255)), (LARGEUR//2-150, 10))
      options.append(fenetre.blit(font_1.render("Volume", 1, (50, 50, 50)), (50, 80)))
      icon_volume = pygame.draw.rect(fenetre, (80, 80, 80), (options[id_tab].x+300, options[id_tab].y, w, h))
      ligne_son = pygame.draw.line(fenetre, (0, 0, 255), (icon_volume.x+5, icon_volume.y+icon_volume.h//2), (icon_volume.x+icon_volume.w-5, icon_volume.y+icon_volume.h//2), 5)
      pourcentage = str(int(son.volumeActuel()*100))+'%'
      pourcentage_volume = font.render(pourcentage, 1, (255, 255, 255))
      fenetre.blit(pourcentage_volume, (icon_volume.x+icon_volume.w+5, ligne_son.y-pourcentage_volume.get_height()//2))
      
      if x == 0:
         x = (ligne_son.x+(son.volumeActuel()*(ligne_son.w-5)))
      niveau_son = pygame.draw.rect(fenetre, (0, 0, 255), (x, ligne_son.y-h//2, 5, h))

      options.append(fenetre.blit(font_1.render("Changer couleur de fond", 1, (0, 0, 255)), (options[id_tab].x, options[id_tab].y+80)))
      id_tab += 1
      options.append(fenetre.blit(font_1.render("Changer Musique", 1, (0, 0, 255)), (options[id_tab].x, options[id_tab].y+50)))
      id_tab += 1
      options.append(fenetre.blit(font_1.render("Retour", 1, (0, 0, 255)), (LARGEUR-120, HAUTEUR-50)))

      if game == True:
         options.append(fenetre.blit(font_1.render("Aller au menu", 1, (0, 0, 255)), (options[id_tab].x, options[id_tab].y+50)))
         id_tab += 2
         options.append(fenetre.blit(font_1.render("Changer niveau", 1, (0, 0, 255)), (options[id_tab].x, options[id_tab].y+50)))
      
      return ligne_son, niveau_son, icon_volume, options

   
def choixNiveau(fond, tab_plateau, joueur, laser, retour):
   LARGEUR = 500
   HAUTEUR = 500

   stop = False
   niveau = 0
   fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
   pygame.display.set_caption("Choix du niveaux")

   p_niveaux = []
   
   font = pygame.font.Font(None, 48)
   font_2 = pygame.font.Font(None, 32)

   p_niveaux.append(fenetre.blit(font.render("Facile", 1, (255, 255, 255)), (10, 100)))
   p_niveaux.append(fenetre.blit(font.render("Moyen", 1, (255, 200, 200)), (10, 150)))
   p_niveaux.append(fenetre.blit(font.render("Difficile", 1, (255, 150, 150)), (10, 200)))
   p_niveaux.append(fenetre.blit(font.render("Pro", 1, (255, 100, 100)), (10, 250)))
   p_niveaux.append(fenetre.blit(font.render("Extrême", 1, (255, 50, 50)), (10, 300)))
   p_niveaux.append(fenetre.blit(font.render("Dieux Grecs", 1, (255, 0, 0)), (10, 350)))
   p_niveaux.append(fenetre.blit(font.render("Personnalisé", 1, (150, 0, 255)), (10, 400)))

   vu_laser = True

   while not stop:

      fenetre.fill((200, 200, 200))

      titre = font.render("Choix niveau", 1, (0, 0, 255))

      fenetre.blit(titre, ((LARGEUR//2)-(titre.get_width()//2), 10))
      fenetre.blit(font.render("Facile", 1, (255, 255, 255)), (10, 100))
      fenetre.blit(font.render("Moyen", 1, (255, 200, 200)), (10, 150))
      fenetre.blit(font.render("Difficile", 1, (255, 150, 150)), (10, 200))
      fenetre.blit(font.render("Pro", 1, (255, 100, 100)), (10, 250))
      fenetre.blit(font.render("Extrême", 1, (255, 50, 50)), (10, 300))
      fenetre.blit(font.render("Dieux Grecs", 1, (255, 0, 0)), (10, 350))
      fenetre.blit(font.render("Personnalisé", 1, (150, 0, 255)), (10, 400))

      vu_laser_t = font_2.render("trajet des lasers", 1, (0, 0, 0))
      vu_laser_p = fenetre.blit(vu_laser_t, (LARGEUR-(vu_laser_t.get_width()+10), 100))

      case_vu = pygame.draw.rect(fenetre, (0, 0, 0), (vu_laser_p.x-25, vu_laser_p.y, 20, 20), 2)

      if vu_laser == True:
         pygame.draw.lines(fenetre, (0, 0, 0), False, ((case_vu.x, case_vu.y), (case_vu.x+(case_vu.w//2), (case_vu.y+case_vu.h)), ((case_vu.x+case_vu.w), (case_vu.y-10))), 4)

      if retour == True:
         p_retour = fenetre.blit(font.render("Retour", 1, (0, 200, 0)), (LARGEUR-120, HAUTEUR-50))
   
      for event in pygame.event.get():
         if event.type == QUIT:
            stop = True
            pygame.quit()
            sys.exit()
         if event.type == MOUSEBUTTONDOWN:
            for i, position in enumerate(p_niveaux):
               if event.pos[0] > position.x and event.pos[0] < position.x+position.w and event.pos[1] > position.y and event.pos[1] < position.y+position.h:
                  if i == 0:
                     print("facile")
                     niveau = 1
                  if i == 1:
                     print("moyen")
                     niveau = 2
                  if i == 2:
                     print("difficile")
                     niveau = 3
                  if i == 3:
                     print("pro")
                     niveau = 4
                  if i == 4:
                     print("extreme")
                     niveau = 5
                  if i == 5:
                     print("dieux grecs")
                     niveau = 6
                  if tab_plateau != None:
                     joueur.clear()
                     laser.clear()
                     tab_plateau.clear()

                  joueur = Joueur()
                  laser = Laser()
                  tab_plateau = Plateau()
                  tab_plateau.vu_laser = vu_laser
                  if i != 6:
                     tab_plateau = creationNiveau(niveau, tab_plateau)
                  else:

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


                     erreur = True
                     nb_atoms = 0

                     while erreur == True:
                        erreur = False

                        try:
                           nb_atoms = int(recup_saisie("Entrez le nombre d'atome que doit contenir le BlackBox", msg_erreur))
                           msg_erreur = ""
                        except ValueError:
                           erreur = True
                           msg_erreur = "Entrée invalide"

                        else:
                           if nb_atoms >= taille_tab:
                              erreur = True
                              msg_erreur = "Le nombre d'atome doit être inférieur à "+str(taille_tab)
                           elif nb_atoms <= 0:
                              erreur = True
                              msg_erreur = "Le nombre d'atome doit être supérieur à 0"

                     tab_plateau.nb_atomes = nb_atoms
                     tab_plateau.creaTab(taille_tab)
                     tab_plateau.atomesAlea()
                     initPlateau(2, tab_plateau)

                  return tab_plateau, joueur, laser, 1
            
            if event.pos[0] > case_vu.x and event.pos[0] < case_vu.x+case_vu.w and event.pos[1] > case_vu.y and event.pos[1] < case_vu.y+case_vu.h:
               vu_laser = not vu_laser

            if retour == True:
               if event.pos[0] > p_retour.x and event.pos[0] < p_retour.x+p_retour.w and event.pos[1] > p_retour.y and event.pos[1] < p_retour.y+p_retour.h:
                  return tab_plateau, joueur, laser, 0

      pygame.display.update()


def changerMusique(son):
   LARGEUR = 600
   HAUTEUR = 500

   fps = pygame.time.Clock()

   fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
   pygame.display.set_caption("Choix de la musique")


   num_musique_t = str(son.getIdSong(1))

   stop = False

   font = pygame.font.Font(None, 48)
   font_2 = pygame.font.Font(None, 32)

   titre = font.render("Changer musique :", 1, (0, 0, 0))

   musique_partie = font.render("Partie", 1, (0, 0, 0))
   musique_menu = font.render("Menu", 1, (0, 0, 0))

   musique = True
   
   y = HAUTEUR//2
   x_cercle = 300
   taille_cercle = 50
   taille = taille_cercle-10
   x_fleche_g = x_cercle-(taille_cercle+taille_cercle)
   x_fleche_d = x_cercle+(taille_cercle)+10
   x_play = x_cercle-(taille_cercle//4)
   color_play = (0, 255, 0)
   play_song = False

   jouer_musique = True

   alea = font.render("Aléatoire", 1, (0, 0, 255))

   y_texte = 80
   op = 1

   while not stop:

      fenetre.fill((255, 255, 255))

      titre_p = fenetre.blit(titre, ((LARGEUR//2)-titre.get_width()//2, 10))
      terminer = fenetre.blit(font_2.render("Terminer", 1, (0, 0, 0)), (LARGEUR-130, HAUTEUR-50))
      choix_g = pygame.draw.polygon(fenetre, (0, 0, 0), ((titre_p.x, y_texte+15), (titre_p.x+15, y_texte+30), (titre_p.x+15, y_texte)))
      choix_d = pygame.draw.polygon(fenetre, (0, 0, 0), (((titre_p.x+titre_p.w)+15, y_texte+15), ((titre_p.x+titre_p.w), y_texte+30), ((titre_p.x+titre_p.w), y_texte)))

      alea_p = fenetre.blit(alea, ((LARGEUR//2)-(alea.get_width()//2), HAUTEUR-150))

      nb_musics_game = font.render(str(son.getIdSong(1)+1)+"/"+str(son.getNbSongs(1)), 1, (0, 0, 0))
      nb_musics_menu = font.render(str(son.getIdSong(2)+1)+"/"+str(son.getNbSongs(2)), 1, (0, 0, 0))
      
      if musique == True:
         op = 1
         fenetre.blit(musique_partie, ((LARGEUR//2)-musique_partie.get_width()//2, y_texte))
         fenetre.blit(nb_musics_game, ((LARGEUR//2)-nb_musics_game.get_width()//2, HAUTEUR-70))
      elif musique == False:
         op = 2
         fenetre.blit(musique_menu, ((LARGEUR//2)-musique_menu.get_width()//2, y_texte))
         fenetre.blit(nb_musics_menu, ((LARGEUR//2)-nb_musics_menu.get_width()//2, HAUTEUR-70))

      if play_song == True:
         color_play = (0, 255, 0)
         pygame.draw.polygon(fenetre , color_play, ((x_play+taille, y), (x_play, y+taille), (x_play, y-taille)))
      else:
         son.stopAllSong()
         color_play = (255, 0, 0)
         pygame.draw.rect(fenetre, color_play, (x_cercle-(taille_cercle//2), y-(taille_cercle//2), taille_cercle, taille_cercle))

      play = pygame.draw.circle(fenetre, color_play, (x_cercle, y), taille_cercle, 2)

      fleche_g = pygame.draw.polygon(fenetre, (150, 0, 150), ((x_fleche_g, y), (x_fleche_g+taille, y+taille), (x_fleche_g+taille, y-taille)))
      fleche_d = pygame.draw.polygon(fenetre, (150, 0, 150), ((x_fleche_d+taille, y), (x_fleche_d, y+taille), (x_fleche_d, y-taille)))

      for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()
         if event.type == MOUSEBUTTONDOWN:

            if event.pos[0] >= fleche_g.x and event.pos[0] < fleche_g.x+fleche_g.w and event.pos[1] >= fleche_g.y and event.pos[1] < fleche_g.y+fleche_g.h:
               print("flèche gauche")
               play_song = False
               son.setIdSong(op, 2)
            if event.pos[0] >= fleche_d.x and event.pos[0] < fleche_d.x+fleche_d.w and event.pos[1] >= fleche_d.y and event.pos[1] < fleche_d.y+fleche_d.h:
               print("flèche droite")
               play_song = False
               son.setIdSong(op, 1)
            if event.pos[0] >= play.x and event.pos[0] < play.x+play.w and event.pos[1] >= play.y and event.pos[1] < play.y+play.h:
               print("play")
               son.music_random = False
               jouer_musique = True
               play_song = not play_song
               son.playSong(op)
            if event.pos[0] >= choix_g.x and event.pos[0] < choix_g.x+choix_g.w and event.pos[1] >= choix_g.y and event.pos[1] < choix_g.y+choix_g.h:
               print("choix gauche")
               play_song = False
               son.stopAllSong()
               musique = not musique
            if event.pos[0] >= choix_d.x and event.pos[0] < choix_d.x+choix_d.w and event.pos[1] >= choix_d.y and event.pos[1] < choix_d.y+choix_d.h:
               print("choix droite")
               play_song = False
               son.stopAllSong()
               musique = not musique
            if event.pos[0] >= terminer.x and event.pos[0] < terminer.x+terminer.w and event.pos[1] >= terminer.y and event.pos[1] < terminer.y+terminer.h:
               print("Terminer")
               return
            if event.pos[0] >= alea_p.x and event.pos[0] < alea_p.x+alea_p.w and event.pos[1] >= alea_p.y and event.pos[1] < alea_p.y+alea_p.h:
               print("Aléatoire")
               son.music_random = True
               return

      pygame.display.update()
      fps.tick(20)