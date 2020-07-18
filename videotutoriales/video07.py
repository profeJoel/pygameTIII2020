import pygame
from pygame.locals import *

pygame.init() # HOla Cris Holi :D
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("MI PRIMER JUEGO")
reloj = pygame.time.Clock()

#Clase Personaje
class personaje(object):

	def __init__(self, x, y, fuente):
		self.x = x
		self.y = y
		fuente += "/"
		self.quieto = pygame.image.load("img/"+fuente+"standing.png")
		self.ancho = self.quieto.get_width()
		self.alto = self.quieto.get_height()
		self.velocidad = 5

	def dibujar(self, cuadro):
		cuadro.blit(self.quieto,(self.x,self.y))

	def se_mueve_segun(self, k, iz, de, ar, ab):
		if k[iz] and self.x > self.velocidad:
			self.x -= self.velocidad

		if k[de] and self.x < ventana_x - self.ancho - self.velocidad:
			self.x += self.velocidad

		if k[ar] and self.y > self.velocidad:
			self.y -= self.velocidad

		if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
			self.y += self.velocidad

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Dibujar Personaje
	heroe.dibujar(ventana)
	#Se refresca la imagen
	pygame.display.update()

# Inicio Funcion principal

repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:

	# Inicializacion de elementos del juego
	imagen_fondo = pygame.image.load('img/bg1.jpg')
	ruta_musica = "snd/dubstep.mp3"
	musica_fondo = pygame.mixer.music.load(ruta_musica)
	pygame.mixer.music.play(-1)

	#Creación Personaje Héroe
	heroe=personaje(int(ventana_x/2), int(ventana_y/2),"heroe")
	
	
	# Seccion de juego
	esta_jugando=True
	while esta_jugando:
		# control de velocidad del juego
		reloj.tick(27)
		# evento de boton de cierre de ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
		
		teclas=pygame.key.get_pressed()
		heroe.se_mueve_segun(teclas,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
		repintar_cuadro_juego()
# Termina el juego y finaliza los elementos de pygame
pygame.quit()
