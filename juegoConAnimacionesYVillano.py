import pygame

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))

pygame.display.set_caption("MI PRIMER JUEGO")

reloj = pygame.time.Clock()

# es necesario un standar de carga
class personaje(object):

	def __init__(self, x, y, ancho, alto, fuente):
		self.x = x
		self.y = y
		self.ancho = ancho
		self.alto = alto
		self.velocidad = 5
		self.haSaltado = False
		self.impulsoSalto = 10
		self.izquierda = False
		self.derecha = False
		self.contadorPasos = 0

		fuente += "/"
		self.caminaIzquierda = [pygame.image.load("img/"+fuente+"L1.png"),pygame.image.load("img/"+fuente+"L2.png"),pygame.image.load("img/"+fuente+"L3.png"),pygame.image.load("img/"+fuente+"L4.png"),pygame.image.load("img/"+fuente+"L5.png"),pygame.image.load("img/"+fuente+"L6.png"),pygame.image.load("img/"+fuente+"L7.png"),pygame.image.load("img/"+fuente+"L8.png"),pygame.image.load("img/"+fuente+"L9.png")]
		self.caminaDerecha = [pygame.image.load("img/"+fuente+"R1.png"),pygame.image.load("img/"+fuente+"R2.png"),pygame.image.load("img/"+fuente+"R3.png"),pygame.image.load("img/"+fuente+"R4.png"),pygame.image.load("img/"+fuente+"R5.png"),pygame.image.load("img/"+fuente+"R6.png"),pygame.image.load("img/"+fuente+"R7.png"),pygame.image.load("img/"+fuente+"R8.png"),pygame.image.load("img/"+fuente+"R9.png")]
		self.quieto = pygame.image.load("img/"+fuente+"standing.png")

	def dibujar(self, cuadro):
		if self.contadorPasos + 1 > 27:
			self.contadorPasos = 0

		if self.izquierda:
			cuadro.blit(self.caminaIzquierda[self.contadorPasos//3],(self.x,self.y))
			self.contadorPasos += 1
		elif self.derecha:
			cuadro.blit(self.caminaDerecha[self.contadorPasos//3],(self.x,self.y))
			self.contadorPasos += 1
		else:
			cuadro.blit(self.quieto, (self.x,self.y))

	def capturar_movimiento(self, k, iz, de, ar, ab, salta):
		if k[iz] and self.x > self.velocidad:
			self.x -= self.velocidad
			self.izquierda = True
			self.derecha = False

		elif k[de] and self.x < ventana_x - self.ancho - self.velocidad:
			self.x += self.velocidad
			self.derecha = True
			self.izquierda = False
		else:
			self.izquierda = False
			self.derecha = False
			self.contadorPasos = 0


		if not self.haSaltado:
			if k[ar] and self.y > self.velocidad:
				self.y -= self.velocidad

			if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
				self.y += self.velocidad

			if k[salta]:
				self.haSaltado = True
				self.izquierda = False
				self.derecha = False
				self.contadorPasos = 0
		else:
			if self.impulsoSalto >= -10:
				if self.impulsoSalto < 0:
					self.y -= (self.impulsoSalto**2) * 0.5 * -1
				else:
					self.y -= (self.impulsoSalto**2) * 0.5
				self.impulsoSalto -= 1
			else:
				self.haSaltado = False
				self.impulsoSalto = 10

heroe = personaje(int(ventana_x/2),int(ventana_y/2),64,64,"heroe")
villano = personaje(int(ventana_x/2)+100,int(ventana_y/2),64,64,"villano")


imagen_fondo = pygame.image.load('img/bg.jpg')
musica = pygame.mixer.music.load('snd/mj.mp3')
pygame.mixer.music.play(-1)

def rePintarCuadroJuego():
	ventana.blit(imagen_fondo,(0,0))
	heroe.dibujar(ventana)
	villano.dibujar(ventana)
	pygame.display.update()

run = True
while run:
	reloj.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()

	heroe.capturar_movimiento(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE)

	villano.capturar_movimiento(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_x)

	rePintarCuadroJuego()

pygame.quit()