# -*- coding: utf-8 -*-

import socket
import sys
import threading
import time
from tkinter import *


class RecevoirClient(threading.Thread):
	
	def __init__(self, hist, connexServ):
		self.hist = hist
		self.connexServ = connexServ
		threading.Thread.__init__(self)

	def run(self):

		# global self.hist, self.connexServ

		msg_recu = ''

		while True:
			msg_recu = self.connexServ.recv(1024)
			if msg_recu != "" and msg_recu != b"" and msg_recu != b"\n" and msg_recu != b" \n" and msg_recu != b"\n\n" and msg_recu != b"  \n" and msg_recu != b"   \n" and msg_recu != b"\n\n\n":

				self.hist.config(state = NORMAL)
				self.hist.insert(END,'Lui : ')
				self.hist.insert(END, msg_recu.decode())
				self.hist.config(state = DISABLED)



class cliTchat(threading.Thread):
	# msgEntry = None
	# hist = None
	# connexServ = None

	def setIp(self, ip):
		self.ip = ip

	def run(self):
		#__________FENETRE_______________________________________________________

		fenetre = Tk()
		fenetre.title("Client - BlackTChat")

		#FRAME
		Frm = Frame(fenetre, width = 470, height = 400)
		Frm.grid(row = 0, column = 0)
		Frm.grid_propagate(0)

		#IMAGE
		img = PhotoImage(file = 'Images/fond.gif')
		fond = Label(Frm, image = img)
		fond.place(x = -2, y = -2)

		#FRMHIST
		self.hist = Text(Frm, height = 15, width = 60, state=DISABLED)
		self.hist.place(x = 20, y = 20)


		#FRMMSG
		self.msgEntry = Text(Frm, height = 5, width = 40)
		self.msgEntry.place(x = 20, y = 290)

		send = Button(Frm, text = 'Envoyer')
		send.config(command = self.envoiClient)
		send.place(x = 350, y = 320)



		#___________RESEAU________________________________________________________
		#ipfile = open("ip.txt","r")
		#ip = ipfile.read()
		self.connexServ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connexServ.connect((self.ip,42000))

		#___________THREAD________________________________________________________

		thread_ecoute = RecevoirClient(self.hist, self.connexServ)
		thread_ecoute.daemon = True
		thread_ecoute.start()

		fenetre.mainloop()

	def envoiClient(self):

		# global self.msgEntry, self.hist, self.connexServ

		msg = self.msgEntry.get(1.0,END).encode()

		if msg != b"\n" and msg != b" \n" and msg != b"\n\n" and msg != b"  \n" and msg != b"   \n" and msg != b"\n\n\n":
			self.connexServ.send(msg)

			self.hist.config(state = NORMAL)
			self.hist.insert(END,'Vous : ')
			self.hist.insert(END, self.msgEntry.get(1.0,END))
			self.hist.config(state = DISABLED)

			self.msgEntry.delete(1.0,END)
