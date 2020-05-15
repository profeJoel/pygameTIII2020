import pygame

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))

pygame.display.set_caption("MI PRIMER JUEGO")

imagen_fondo = pygame.image.load('img/bg.jpg')

musica = pygame.mixer.music.load('snd/mj.mp3')
#musica = pygame.mixer.music.load('snd/music.mp3')
pygame.mixer.music.play(-1)

# se inicializa el reloj del juego
clock = pygame.time.Clock()

# definicion objeto personaje
class personaje(object):

	# inicializacion de variables del personaje
	def __init__(self, x, y, ancho, alto):
		self.x = x
		self.y = y
		self.ancho = ancho
		self.alto = alto
		self.velocidad = 5
		self.haSaltado = False
		self.impulsoSalto = 10
		self.izquierda = False
		self.derecho = False
		self.contadorPasos = 0
		# carga de sprites (cada una de los imágenes) para animacion izquierda
		self.caminaIzquierda = [pygame.image.load('img/R1.png'),pygame.image.load('img/R2.png'),pygame.image.load('img/R3.png'),pygame.image.load('img/R4.png'),pygame.image.load('img/R5.png'),pygame.image.load('img/R6.png'),pygame.image.load('img/R7.png'),pygame.image.load('img/R8.png'),pygame.image.load('img/R9.png')]
		# carga de sprites (cada una de los imágenes) para animacion derecha
		self.caminaDerecha = [pygame.image.load('img/L1.png'),pygame.image.load('img/L2.png'),pygame.image.load('img/L3.png'),pygame.image.load('img/L4.png'),pygame.image.load('img/L5.png'),pygame.image.load('img/L6.png'),pygame.image.load('img/L7.png'),pygame.image.load('img/L8.png'),pygame.image.load('img/L9.png')]
		# carga de sprite
		self.deFrente = pygame.image.load('img/standing.png')

	# dibuja al personaje en sus diversos pasos
	def dibujar(self, cuadro):

        # limita la cantidad de pasos realizados 27 iteraciones [0-26]
		if self.contadorPasos + 1 >= 27:
			self.contadorPasos = 0
			
		# Describe la secuencia de imagenes para caminar a la izquierda
		if self.izquierda:
		    # se elige una imagen de la secuencia según corresponda
			cuadro.blit(self.caminaIzquierda[self.contadorPasos//3], (self.x,self.y))
			self.contadorPasos += 1
			
		# Describe la secuencia de imagenes para caminar a la derecha
		elif self.derecha:
		    # se elige una imagen de la secuencia según corresponda
			cuadro.blit(self.caminaDerecha[self.contadorPasos//3], (self.x,self.y))
			self.contadorPasos += 1
			
		# si no es ninguna de las anteriores, el personaje esta simplemente quieto
		else:
			cuadro.blit(self.deFrente,(self.x,self.y))

# se define una rutina para ejecutar cada elemento
def rePintarCuadroJuego():
	# se pinta el fondo
	ventana.blit(imagen_fondo,(0,0))
	# se dibuja el personaje
	heroe.dibujar(ventana)
	# actualiza el cuadro del dibujo
	pygame.display.update()


# se crea personaje llamado "heroe" y sus atributos
heroe = personaje(int(ventana_x/2),int(ventana_y/2),64,64)

R = 50
G = 50
B = 50
radio = 100

run = True
while run:
	clock.tick(27) # implementacion del reloj del juego

	for event in pygame.event.get(): # codigo para evento de cierre
		if event.type == pygame.QUIT:
			run=False

	keys = pygame.key.get_pressed()
	# captura la ejecucion de la animacion para la izquierda
	if keys[pygame.K_LEFT] and heroe.x > heroe.velocidad:
		heroe.x -= heroe.velocidad
		heroe.izquierda = True
		heroe.derecha = False
	
	# captura la ejecucion de la animacion para la derecha
	elif keys[pygame.K_RIGHT] and heroe.x < ventana_x - heroe.ancho - heroe.velocidad:
		heroe.x += heroe.velocidad
		heroe.derecha = True
		heroe.izquierda = False
		
	# captura la ejecucion la imagen fija del personaje
	else: 
		heroe.derecha = False
		heroe.izquierda = False
		heroe.contadorPasos = 0

	# movimientos verticales
	if not heroe.haSaltado:
		if keys[pygame.K_UP] and heroe.y > heroe.velocidad:
			heroe.y -= heroe.velocidad
		if keys[pygame.K_DOWN] and heroe.y < ventana_y - heroe.alto - heroe.velocidad:
			heroe.y += heroe.velocidad
		# captura accion salto
		if keys[pygame.K_SPACE]:
			heroe.haSaltado = True
			heroe.derecha = False
			heroe.izquierda = False
			heroe.contadorPasos = 0
			
	# ejecuta el salto
	else:
		# calcula el salto
		if heroe.impulsoSalto >= -10:
			if heroe.impulsoSalto < 0:
				heroe.y -= (heroe.impulsoSalto**2) * 0.5 * -1
			else:
				heroe.y -= (heroe.impulsoSalto**2) * 0.5
			heroe.impulsoSalto -= 1
		else:
			heroe.haSaltado = False
			heroe.impulsoSalto = 10

	# repinta el cuadro del juego
	rePintarCuadroJuego()

pygame.quit()