import pygame, random
from pygame.locals import *


class Sound():
   dict_sons = dict()
   id_game = 0
   musics_game = []
   id_menu = 0
   musics_menu = []
   id_settings = 0
   musics_settings = []
   nb_musics_menu = 0
   nb_musics_game = 0
   nb_musics_settings = 0
   music_random = True


   def __init__(self, nom_repertoire = "Songs.txt"):
      self.nom_repertoire = nom_repertoire
      self.definirSons(2)
      

   def choixVolume(self, valeur):
      for music in self.musics_game:
         music.set_volume(valeur/100)
      for music in self.musics_menu:
         music.set_volume(valeur/100)
      for music in self.musics_settings:
         music.set_volume(valeur/100)
      self.son_clic.set_volume(valeur/100)


   def volumeActuel(self):
      return self.musics_menu[0].get_volume()


   def definirSons(self, op, id_son = "", nom_son = ""):
      if op == 1:
         sauvegarde_sons = open(self.nom_repertoire, 'a')
         sauvegarde_sons.write(id_son+':'+nom_son+'\n')
         self.dict_sons[id_son] = nom_son
         sauvegarde_sons.close()
      elif op == 2:
         sauvegarde_sons = open(self.nom_repertoire, 'r')
         for son in sauvegarde_sons.readlines():
            
            id_son = son[:son.index(':')]
            nom_son = son[son.index(':')+1:son.index('\n')]
            if id_son == "game":
               self.musics_game.append(pygame.mixer.Sound(nom_son))
            elif id_son == "clic":
               self.son_clic = pygame.mixer.Sound(nom_son)
            elif id_son == "menu":
               self.musics_menu.append(pygame.mixer.Sound(nom_son))
            elif id_son == "settings":
               self.musics_settings.append(pygame.mixer.Sound(nom_son))
         sauvegarde_sons.close()
         self.nb_musics_game = len(self.musics_game)
         self.nb_musics_menu = len(self.musics_menu)
         self.nb_musics_settings = len(self.musics_settings)

   def stopAllSong(self):
      for music in self.musics_game:
         music.stop()

      for music in self.musics_menu:
         music.stop()

      for music in self.musics_settings:
         music.stop()

      self.son_clic.stop()


   def getNbSongs(self, op):
      if op == 1:
         return self.nb_musics_game
      elif op == 2:
         return self.nb_musics_menu


   def setIdSong(self, op, change):
      if op == 1:
         if change == 1:
            self.id_game += 1
         elif change == 2:
            self.id_game -= 1

         if self.id_game > len(self.musics_game)-1:
            self.id_game = 0
         elif self.id_game < 0:
            self.id_game = len(self.musics_game)-1
      elif op == 2:
         if change == 1:
            self.id_menu += 1
         elif change == 2:
            self.id_menu -= 1

         if self.id_menu > len(self.musics_menu)-1:
            self.id_menu = 0
         elif self.id_menu < 0:
            self.id_menu = len(self.musics_menu)-1


   def playSong(self, op):
      self.stopAllSong()

      if self.music_random == True:
         self.id_game = random.randint(0, self.nb_musics_game-1)
         self.id_menu = random.randint(0, self.nb_musics_menu-1)

      if op == 1:
         self.musics_game[self.id_game].play(-1)
      elif op == 2:
         self.musics_menu[self.id_menu].play(-1)
      elif op == 3:
         self.id_settings = random.randint(0, self.nb_musics_settings-1)
         self.musics_settings[self.id_settings].play(-1)


   def getIdSong(self, op):
      if op == 1:
         return self.id_game
      if op == 2:
         return self.id_menu

   def playSongClic(self):
      self.son_clic.play()