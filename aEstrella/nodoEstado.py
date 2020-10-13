from nodo import nodo
from arco import arco
from grafo import grafo

import math


class nodoEstado:
	def __init__(self, nodo, EP, A, n):
		self.nodo = nodo
		self.padre = EP
		self.accion = A
		self.nivel = n
		self.g = -1 #marca de indefinido
		self.h = -1 #marca de indefinido

	def getnodo(self):
		return self.nodo

	def getPadre(self):
		return self.padre

	def getAccion(self):
		return self.accion

	def getNivel(self):
		return self.nivel

	def getSucesores(self):
		return self.nodo.getCaminos()

	def getG(self):
		return self.g

	def getH(self):
		return self.h

	def getF(self):
		return (self.g+self.h)

	#def setG(self,estado):
	def setG(self,estado,peso):
		if estado is None:
			self.g = -1
		else:
			objetivo = estado.getnodo()
			G_acumulado = estado.getG() if estado.getG() > 0 else 0
			#self.g = G_acumulado + math.sqrt(((objetivo.getY()-self.nodo.getY())**2) + ((objetivo.getX()-self.nodo.getX())**2))
			self.g = G_acumulado + peso

	def setH(self,estado):
		if estado is None:
			self.h = -1
		else:
			objetivo = estado.getnodo()
			self.h = math.sqrt(((objetivo.getY()-self.nodo.getY())**2) + ((objetivo.getX()-self.nodo.getX())**2))

	def __eq__(self, estado):
		if estado == None:
			return False
		return self.nodo == estado.getnodo()

	def __str__(self):
		return "Estado Actual" + str(self.nodo) + "\nAccion:\n"+ self.accion + "\n Nivel: " + str(self.nivel) +"\n g(e): " + str(self.g) +" + h(e): " + str(self.h) + " = f(e): " + str(self.g+self.h) + "\n"