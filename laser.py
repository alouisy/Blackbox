from plateau import *

class Laser(Plateau):
	coordonnees_laser = []
	texte_laser = ""

	def __init__(self):
		pass

	def clear(self):
		self.coordonnees_laser.clear()

	def set_coord(self, coordonnees_laser):
		self.coordonnees_laser.append(coordonnees_laser)