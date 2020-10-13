import arco

class nodo:
	def __init__(self, x, y, nombre):
		self.x = x
		self.y = y
		self.nombre = nombre
		self.caminos = []

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getNombre(self):
		return self.nombre

	def setCamino(self,camino):
		self.caminos.append(camino)

	def getCamino(self,indice):
		return self.camino[indice]

	def getCaminos(self):
		return self.caminos

	def __eq__(self, estado):
		if estado == None:
			return False
		return self.x == estado.getX() and self.y == estado.getY()

	def __str__(self):
		return "(" + self.nombre + ") = <"+str(self.x)+","+str(self.y)+">"