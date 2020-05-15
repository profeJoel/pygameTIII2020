import pygame

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))

pygame.display.set_caption("MI PRIMER JUEGO")

reloj = pygame.time.Clock()

class personaje(object):

	def __init__(self, x, y, ancho, alto):
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

		self.caminaIzquierda = [pygame.image.load("img/L1.png"),pygame.image.load("img/L2.png"),pygame.image.load("img/L3.png"),pygame.image.load("img/L4.png"),pygame.image.load("img/L5.png"),pygame.image.load("img/L6.png"),pygame.image.load("img/L7.png"),pygame.image.load("img/L8.png"),pygame.image.load("img/L9.png")]
		self.caminaDerecha = [pygame.image.load("img/R1.png"),pygame.image.load("img/R2.png"),pygame.image.load("img/R3.png"),pygame.image.load("img/R4.png"),pygame.image.load("img/R5.png"),pygame.image.load("img/R6.png"),pygame.image.load("img/R7.png"),pygame.image.load("img/R8.png"),pygame.image.load("img/R9.png")]
		self.quieto = pygame.image.load("img/standing.png")

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

heroe = personaje(int(ventana_x/2),int(ventana_y/2),64,64)


imagen_fondo = pygame.image.load('img/bg.jpg')
musica = pygame.mixer.music.load('snd/mj.mp3')
pygame.mixer.music.play(-1)

def rePintarCuadroJuego():
	ventana.blit(imagen_fondo,(0,0))
	heroe.dibujar(ventana)
	pygame.display.update()

run = True
while run:
	reloj.tick(27)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()


	if keys[pygame.K_LEFT] and heroe.x > heroe.velocidad:
		heroe.x -= heroe.velocidad
		heroe.izquierda = True
		heroe.derecha = False

	elif keys[pygame.K_RIGHT] and heroe.x < ventana_x - heroe.ancho - heroe.velocidad:
		heroe.x += heroe.velocidad
		heroe.derecha = True
		heroe.izquierda = False
	else:
		heroe.izquierda = False
		heroe.derecha = False
		heroe.contadorPasos = 0


	if not heroe.haSaltado:
		if keys[pygame.K_UP] and heroe.y > heroe.velocidad:
			heroe.y -= heroe.velocidad

		if keys[pygame.K_DOWN] and heroe.y < ventana_y - heroe.alto - heroe.velocidad:
			heroe.y += heroe.velocidad

		if keys[pygame.K_SPACE]:
			heroe.haSaltado = True
			heroe.izquierda = False
			heroe.derecha = False
			heroe.contadorPasos = 0
	else:
		if heroe.impulsoSalto >= -10:
			if heroe.impulsoSalto < 0:
				heroe.y -= (heroe.impulsoSalto**2) * 0.5 * -1
			else:
				heroe.y -= (heroe.impulsoSalto**2) * 0.5
			heroe.impulsoSalto -= 1
		else:
			heroe.haSaltado = False
			heroe.impulsoSalto = 10

	rePintarCuadroJuego()

pygame.quit()