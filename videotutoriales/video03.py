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
	pygame.display.update()

# Inicio Funcion principal

repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:

	# Inicializacion de elementos del juego
	imagen_fondo = pygame.image.load('img/bg1.jpg')
	#se agrega música de fonde
	ruta_musica = "snd/dubstep.mp3"
	musica_fondo = pygame.mixer.music.load(ruta_musica)
	pygame.mixer.music.play(-1)

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
