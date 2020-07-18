import pygame
from pygame.locals import *

pygame.init() # HOla Cris Holi :D
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("MI PRIMER JUEGO")
reloj = pygame.time.Clock()

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Se crea un rectángulo (explicar colores RGB)
	pygame.draw.rect(ventana,(255,0,0), (x1,y1,ancho1,alto1))
	pygame.draw.rect(ventana,(130,12,85), (x2,y2,ancho2,alto2))
	#Dibujar Personaje
	ventana.blit(imagen_personaje,(x,y))
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

	#Variables para figuras (usar así para luego retomar en "Clases y objetos")
	#(Jugar con las ubicaciones, tamaños y colores)
	x1=50
	y1=50
	alto1=60
	ancho1=40
	x2=500
	y2=300
	alto2=80
	ancho2=100

	#Variables personaje
	x=400
	y=400
	alto=64
	ancho=64
	imagen_personaje=pygame.image.load("img/heroe/standing.png")

	# Seccion de juego
	esta_jugando=True
	while esta_jugando:
		# control de velocidad del juego
		reloj.tick(27)
		# evento de boton de cierre de ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
		repintar_cuadro_juego()
# Termina el juego y finaliza los elementos de pygame
pygame.quit()
