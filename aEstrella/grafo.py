from nodo import nodo
from arco import arco

class grafo:
	def __init__(self, archivoGrafo):
		self.nodos = []
		self.arcos = []
		self.setGrafoByMatrix(archivoGrafo)

	def getNodo(self,indice):
		return self.nodos[indice]

	def getArco(self,indice):
		return self.arcos[indice]

	def NuevoNodo(self, x, y, nombre):
		nodoNuevo = nodo(x,y,nombre)
		self.nodos.append(nodoNuevo)

	def NuevoArco(self, origen, destino, atributo):
		arcoNuevo = arco(origen,destino,atributo)
		origen.setCamino(arcoNuevo)
		self.arcos.append(arcoNuevo)

	def encontrarNodo(self,nodo):
		if nodo in self.nodos:
			return self.nodos[self.nodos.index(nodo)]
		else:
			self.NuevoNodo(nodo.getX(), nodo.getY(), nodo.getNombre())
			return self.nodos[self.nodos.index(nodo)]

	def setGrafoByMatrix(self, archivo):

		with open(archivo) as en_archivo:
			for linea in en_archivo:
				posicion = linea.split(' ')
				x1 = float(posicion[0])
				y1 = float(posicion[1])

				nodoaux = nodo(x1,y1,posicion[2])
				if nodoaux in self.nodos:
					Origen = self.nodos[self.nodos.index(nodoaux)]
				else:
					self.NuevoNodo(x1,y1,posicion[2])
					Origen = self.nodos[self.nodos.index(nodoaux)]

				x1 = float(posicion[3])
				y1 = float(posicion[4])

				nodoaux = nodo(x1,y1,posicion[5])
				if nodoaux in self.nodos:
					Destino = self.nodos[self.nodos.index(nodoaux)]
				else:
					self.NuevoNodo(x1,y1,posicion[5])
					Destino = self.nodos[self.nodos.index(nodoaux)]

				atributo = float(posicion[6])

				self.NuevoArco(Origen, Destino, atributo)

	def setGrafoByTuplas(self, archivo):
		print("por construir...")

	def getCamino(self,indice):
		return self.camino[indice]

	def __str__(self):
		out = "\nNodos:\n"
		for n in self.nodos:
			out += str(n) + " = ["
			for s in n.getCaminos():
				out += str(s) + ", "
			out += "]\n"

		out += "\nArcos:\n"
		for a in self.arcos:
			out += str(a) + "\n"

		return "EL grafo es:\n" + out
