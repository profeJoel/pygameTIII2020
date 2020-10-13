import nodo

class arco:
	def __init__(self, origen, destino, distancia):
		self.origen = origen
		self.destino = destino
		self.distancia = distancia

	def getOrigen(self):
		return self.origen

	def getDestino(self):
		return self.destino

	def getDistancia(self):
		return self.distancia

	def setDistancia(self,distancia):
		self.distancia = distancia

	def getCamino(self,indice):
		return self.camino[indice]

	def __eq__(self, estado):
		if estado == None:
			return False
		return self.origen == estado.getOrigen() and self.destino == estado.getDestino()

	def __str__(self):
		return "|" + str(self.origen) + " -> " + str(self.destino) + "| = (" + str(self.distancia) + ")"