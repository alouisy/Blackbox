import random, copy
from plateau import *


def deplacementLaser(tab_plateau, x, y, deplacement):
    if deplacement == 1:
        return x, y+1
    elif deplacement == 2:
        return x, y-1
    elif deplacement == 3:
        return x+1, y
    elif deplacement == 4:
        return x-1, y
    return x, y

def gestionLaser(tab_plateau, laser, clic):

    for t, coord_laser in enumerate(laser.coordonnees_laser):
        x = coord_laser[0]
        y = coord_laser[1]
        deplacement = coord_laser[2]
        laser.texte_laser = ""

        stop = False
        tours = 0
        tab_plateau.pose_x = x
        tab_plateau.pose_y = y
        coord_laser = []
        coord_laser.append((tab_plateau.plateau_pose[y][x].x+tab_plateau.taille_carreau//2,tab_plateau.plateau_pose[y][x].y+tab_plateau.taille_carreau//2))

        x, y = deplacementLaser(tab_plateau, x, y, deplacement)

        while stop == False:

            coord_laser.append((tab_plateau.plateau_pose[y][x].x+tab_plateau.taille_carreau//2,tab_plateau.plateau_pose[y][x].y+tab_plateau.taille_carreau//2))
            if tab_plateau.plateau_ref[y][x]  == 1 or tab_plateau.plateau_ref[y][x] == 3 or tours == len(tab_plateau.plateau_ref)*2 or deplacement == 5:
                stop = True
                if tab_plateau.plateau_ref[y][x] == 3:
                    tab_plateau.message = "A"
                    laser.texte_laser = "Rayon absorbé"

            elif tab_plateau.plateau_ref[y][x] == 2:

                x, y = deplacementLaser(tab_plateau, x, y, deplacement)

            else:

                deplacement, laser.texte_laser = collisionAtomes(tab_plateau, x, y, deplacement)
                x, y = deplacementLaser(tab_plateau, x, y, deplacement)

        tab_plateau.pose_v = x
        tab_plateau.pose_w = y

        if len(coord_laser) > 2:
            
            tab_plateau.affiche_laser(coord_laser)

        if clic == 255 and t == len(laser.coordonnees_laser)-1:
            tab_plateau.gestion_message()
            

        if tab_plateau.plateau_jeu[y][x] == 1:
            tab_plateau.plateau_jeu[y][x] = 4
        tab_plateau.message = ""

    tab_plateau.affiche_message()


def Fdeplacement(deplacement, x, y, cote):
    if cote == 1:
        if deplacement == 1:
            return 4
        elif deplacement == 3:
            return 2
    
    elif cote == 2:
        if deplacement == 1:
            return 3
        elif deplacement == 4:
            return 2
    
    elif cote == 3:
        if deplacement == 3:
            return 1
        elif deplacement == 2:
            return 4
            
    elif cote == 4:
        if deplacement == 4:
            return 1
        elif deplacement == 2:
            return 3


def collisionAtomes(tab_plateau, x, y, deplacement):
    texte_laser = "Rayon dévié"

    nb_atomes = 0

    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if j < 0 or i < 0 or j > tab_plateau.nb_cases-1 or i > tab_plateau.nb_cases-1:
                continue
            elif tab_plateau.plateau_ref[i][j] == 3:
                nb_atomes += 1

    if nb_atomes > 1:
        tab_plateau.message += "R"
        texte_laser = "Rayon réfléchit"
        return 5, texte_laser


    for atome in tab_plateau.tab_atomes:
        i = atome[0]
        j = atome[1]
        atome_proche = 0
        cote = 0
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                if tab_plateau.plateau_ref[k][l] == 3:
                    atome_proche += 1
                if (k != i and l != j):#extremite (haut_gauche, haut_droite, bas_gauche, bas_droite)
                    cote += 1
                if k == y and l == x:
                    if (k == i or l == j) or atome_proche > 1:#extremite (haut, bas, gauche, droite)
                        if deplacement == 1 and tab_plateau.plateau_ref[k+1][l] == 3:
                            tab_plateau.message = "A"
                            texte_laser = "Rayon absorbé"
                        elif deplacement == 2 and tab_plateau.plateau_ref[k-1][l] == 3:
                            tab_plateau.message = "A"
                            texte_laser = "Rayon absorbé"
                        elif deplacement == 3 and tab_plateau.plateau_ref[k][l+1] == 3:
                            tab_plateau.message = "A"
                            texte_laser = "Rayon absorbé"
                        elif deplacement == 4 and tab_plateau.plateau_ref[k][l-1] == 3:
                            tab_plateau.message = "A"
                            texte_laser = "Rayon absorbé"
                        else:
                            tab_plateau.message = "R"
                            texte_laser = "Rayon réfléchit"
                        return 5, texte_laser
                    return Fdeplacement(deplacement, x, y, cote), texte_laser


def bordAtomes(tab_plateau):
    for i, ligne in enumerate(tab_plateau):
        for j, val in enumerate(ligne):
            if val == 3:
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        if tab_plateau[k][l] == 2:
                            tab_plateau[k][l] = 5


def placement_atome_alea():
    
    nb_atomes, taille_tab = Choix_niveau()

    tab_plateau = plateau(taille_tab)

    for i in range(nb_atomes-1):
        x = random.randint(1, len(tab_plateau.plateau_ref)-2)
        y = random.randint(1, len(tab_plateau.plateau_ref)-2)
        tab_plateau.plateau_ref[y][x] = 3
        tab_plateau.plateau_jeu[y][x] = 3
    return tab_plateau


def verificationAtomes(tab_plateau):
    for i in range(1, len(tab_plateau.plateau_ref)-1):
        for j in range(1, len(tab_plateau.plateau_ref)-1):
            if tab_plateau.plateau_jeu[i][j] == 8:
                if tab_plateau.plateau_ref[i][j] == 3:
                    tab_plateau.affiche_clic(i, j, 4)
                else:
                    tab_plateau.affiche_clic(i, j, 9)
