from collections import deque
import sys
import os
import math
from time import sleep

from nodo import nodo
from arco import arco
from grafo import grafo
from nodoEstado import nodoEstado

sys.setrecursionlimit(500000)#999

def ordenarPorF(e):
		return e.getF()

class Busqueda:
	
	def __init__(self, nodoOrigen, nodoFinal, archivoGrafo):
		self.tablero = grafo(archivoGrafo)
		self.estadoInicial = nodoEstado(self.tablero.encontrarNodo(nodoOrigen),None,"Origen",1)
		self.estadoFinal= nodoEstado(self.tablero.encontrarNodo(nodoFinal),None,"Final",None)
		self.estadoInicial.setG(self.estadoInicial,0)
		self.estadoInicial.setH(self.estadoFinal)
		#self.tablero.getGrafo()
		#print(self.tablero)
		self.estadoActual = None
		self.historial=[]
		self.colaEstados=deque()

	def add(self,ET):#,direccion):
		self.colaEstados.append(ET)
		self.historial.append(ET)

	def pop(self):
		return self.colaEstados.popleft()

	def mover(self, sucesor): # valor de los arcos del estado Actual
		nuevoNodo = sucesor.getDestino()
		nuevoEstado = nodoEstado(nuevoNodo, self.estadoActual, "De " + self.estadoActual.getnodo().getNombre() + " a " + nuevoNodo.getNombre(), self.estadoActual.getNivel()+1)
		nuevoEstado.setG(self.estadoActual, sucesor.getDistancia())
		return nuevoEstado

	def estaEnHistorial(self,estado): # retorna un boleano
		return True if estado in self.historial else False

	def esFinal(self):
		return self.estadoActual == self.estadoFinal

	def buscarPadres(self, EA):
		if(EA.getPadre() == None):
			print(EA)
		else:
			padre = EA.getPadre() # posicion del padre del padre en el arreglo historial
			self.buscarPadres(padre)
			print(EA)

	def traspasarACola(self, lista,N):
		for estado in lista:
			self.add(estado)
		for n in range(0,N):
			self.colaEstados.appendleft(self.colaEstados.pop())


	def busqueda(self):
		self.add(self.estadoInicial)
		self.busqueda_a_estrella(self.pop(),1)

	def busqueda_a_estrella(self, EI, i): #recursiva
		self.estadoActual = EI # genera cambio de estado
		#print(self.estadoActual)
		colaTransitoria = []

		if(self.esFinal()):
			self.buscarPadres(EI)
			print("BUSQUEDA PROFUNDIDAD Ha llegado a un estado Final!!!\nCantidad de estados alcanzados: "+ str(len(self.historial)) + " \nTamanno de la colaEstados: " + str(len(self.colaEstados)) + " \nIteraciones : " + str(i) + "\nPeso Total Acumulado: " + str(self.estadoActual.getF()))
		else:
			#calcular los sucesores del estado actual
			sucesores = self.estadoActual.getSucesores()
			N=0
			for sucesor in sucesores:
				estadoTransitorio = self.mover(sucesor)
				#estadoTransitorio.setG(self.estadoActual)
				if not self.estaEnHistorial(estadoTransitorio):
					estadoTransitorio.setH(self.estadoFinal)
					colaTransitoria.append(estadoTransitorio)
					N+=1

			#ajuste cola de prioridad - Hijos Primero
			colaTransitoria.sort(key=ordenarPorF)

			self.traspasarACola(colaTransitoria,N)

			return self.busqueda_a_estrella(self.pop(),i+1)


origen = nodo(-3,4,"I")
destino = nodo(3,-2,"F")
experiento = Busqueda(origen, destino, "g1.dat")
experiento.busqueda()