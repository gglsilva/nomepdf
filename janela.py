#!/usr/bin/python
##coding: utf-8

from tkinter import *

class Application:
	def __init__(self, master=None):
		self.Container01 = Frame(master)
		self.Container01["pady"] = 10
		self.Container01.pack()

		self.Container02 = Frame(master)
		self.Container02["pady"] = 10
		self.Container02.pack()

		self.Container03 = Frame(master)
		#self.Container03["padx"] = 20
		self.Container03.pack()

		self.Container04 = Frame(master)
		self.Container04["pady"] = 10
		self.Container04.pack(side=BOTTOM)

		##### Container 01
		self.titulo = Label(self.Container01, text="Dividir Boletos")
		self.titulo.pack(side=RIGHT)

		#### Conteainer 02
		self.origem = Label(self.Container02, text="Origem:")
		self.origem.pack(side=LEFT)

		self.ent_origem = Entry(self.Container02)
		self.ent_origem["width"] = 60
		self.ent_origem.pack(side=LEFT)

		#### Container 03
		self.destino = Label(self.Container03, text="Destino:")
		self.destino.pack(side=LEFT)

		self.ent_destino = Entry(self.Container03)
		self.ent_destino["width"] = 60
		self.ent_destino.pack(side=LEFT)


		#### Container 04
		self.bt_cancel = Button(self.Container04, text="Cancelar")
		self.bt_cancel["width"] = 10
		self.bt_cancel.pack(side=LEFT, padx="40")

		self.bt_ok = Button(self.Container04, text="OK")
		self.bt_ok["width"] = 10
		self.bt_ok["command"] = self.buscarPDF
		self.bt_ok.pack(side=LEFT, padx="40")

	def buscarPDF(self):
		caminho = self.ent_origem.get()
		print(caminho)

if __name__ == "__main__":
	root = Tk()
	Application(root)
	root.mainloop()
