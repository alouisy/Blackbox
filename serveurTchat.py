# -*- coding: utf-8 -*-

import socket
import sys
import threading
import time
from tkinter import *


class RecevoirServ(threading.Thread):
	
	def __init__(self, hist, connexClient):
		self.hist = hist
		self.connexClient = connexClient
		threading.Thread.__init__(self)

	def run(self):

		# global self.hist, self.connexClient

		msg_recu = ''

		while True:
			msg_recu = self.connexClient.recv(1024)
			if msg_recu != "" and msg_recu != b"" and msg_recu != b"\n" and msg_recu != b" \n" and msg_recu != b"\n\n" and msg_recu != b"  \n" and msg_recu != b"   \n" and msg_recu != b"\n\n\n":

				self.hist.config(state = NORMAL)
				self.hist.insert(END,'Lui : ')
				self.hist.insert(END, msg_recu.decode())
				self.hist.config(state = DISABLED)



class servTchat(threading.Thread):

	# msgEntry = None
	# hist = None
	# connexClient = None

	def run(self):

		#__________FENETRE_______________________________________________________

		fenetre = Tk()
		fenetre.title("Serveur - BlackTChat")

		#FRAME
		Frm = Frame(fenetre, width = 470, height = 400, relief = SOLID)
		Frm.grid(row = 0, column = 0)
		Frm.grid_propagate(0)

		#IMAGE
		img = PhotoImage(file = 'Images/fond.gif')
		fond = Label(Frm, image = img)
		fond.place(x = -2, y = -2)

		#FRMHIST
		self.hist = Text(Frm, height = 15, width = 60, state = DISABLED)
		self.hist.place(x = 20, y = 20)


		#FRMMSG
		self.msgEntry = Text(Frm, height = 5, width = 40)
		self.msgEntry.place(x = 20, y = 290)

		send = Button(Frm, text = 'Envoyer')
		send.config(command = self.envoiServ)
		send.place(x = 350, y = 320)

		#___________RESEAU________________________________________________________

		connexUn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connexUn.bind(('',42000))
		connexUn.listen(5)
		self.connexClient, infoConnex = connexUn.accept()

		#___________THREAD________________________________________________________

		thread_ecoute = RecevoirServ(self.hist, self.connexClient)
		thread_ecoute.daemon = True
		thread_ecoute.start()

		fenetre.mainloop()
			
	def envoiServ(self):

		# global self.msgEntry, self.hist, self.connexClient

		msg = self.msgEntry.get(1.0,END).encode()

		if msg != b"\n" and msg != b" \n" and msg != b"\n\n" and msg != b"  \n" and msg != b"   \n" and msg != b"\n\n\n":
			self.connexClient.send(msg)

			self.hist.config(state = NORMAL)
			self.hist.insert(END,'Vous : ')
			self.hist.insert(END,self.msgEntry.get(1.0,END))
			self.hist.config(state = DISABLED)

			self.msgEntry.delete(1.0,END)

