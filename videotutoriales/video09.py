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
		self.velocidad = 5
		#Atributos para salto
		self.ha_saltado = False
		self.impulso_salto = 10
		#Atributos para animación de Sprites
		self.va_izquierda = False
		self.va_derecha = False
		self.contador_pasos = 0
		fuente += "/"
		self.camina_izquierda = [pygame.image.load("img/"+fuente+"L1.png"),pygame.image.load("img/"+fuente+"L2.png"),pygame.image.load("img/"+fuente+"L3.png"),pygame.image.load("img/"+fuente+"L4.png"),pygame.image.load("img/"+fuente+"L5.png"),pygame.image.load("img/"+fuente+"L6.png"),pygame.image.load("img/"+fuente+"L7.png"),pygame.image.load("img/"+fuente+"L8.png"),pygame.image.load("img/"+fuente+"L9.png")]
		self.camina_derecha = [pygame.image.load("img/"+fuente+"R1.png"),pygame.image.load("img/"+fuente+"R2.png"),pygame.image.load("img/"+fuente+"R3.png"),pygame.image.load("img/"+fuente+"R4.png"),pygame.image.load("img/"+fuente+"R5.png"),pygame.image.load("img/"+fuente+"R6.png"),pygame.image.load("img/"+fuente+"R7.png"),pygame.image.load("img/"+fuente+"R8.png"),pygame.image.load("img/"+fuente+"R9.png")]
		self.quieto = pygame.image.load("img/"+fuente+"standing.png")
		self.ancho = self.quieto.get_width()
		self.alto = self.quieto.get_height()

	def dibujar(self, cuadro):
		#Son 9 imágenes de la animación, para que cada una dure 3 vueltas de ciclo se multiplica por 3
		if self.contador_pasos + 1 > 27:
			self.contador_pasos = 0

		if self.va_izquierda:
			cuadro.blit(self.camina_izquierda[self.contador_pasos//3],(self.x,self.y))
			self.contador_pasos += 1
		elif self.va_derecha:
			cuadro.blit(self.camina_derecha[self.contador_pasos//3],(self.x,self.y))
			self.contador_pasos += 1
		else:
			if self.va_derecha:
				cuadro.blit(self.camina_derecha[0],(self.x,self.y))
			elif self.va_izquierda:
				cuadro.blit(self.camina_izquierda[0],(self.x,self.y))
			else:
				cuadro.blit(self.quieto, (self.x,self.y))
			

	def se_mueve_segun(self, k, iz, de, ar, ab, salta):
		if k[iz] and self.x > self.velocidad:
			self.x -= self.velocidad
			#Controles de animación
			self.va_izquierda = True
			self.va_derecha = False

		elif k[de] and self.x < ventana_x - self.ancho - self.velocidad:
			self.x += self.velocidad
			#Controles de animación
			self.va_derecha = True
			self.va_izquierda = False
		else:
			#Controles de animación en caso de dejar de moverse en horizonal
			self.va_izquierda = False
			self.va_derecha = False
			self.contador_pasos = 0


		#Control de Salto

		#Si se reconoce que se ha saltado
		if self.ha_saltado:
			if self.impulso_salto >= -10:
				if self.impulso_salto < 0:
					self.y -= (self.impulso_salto**2) * 0.5 * -1
				else:
					self.y -= (self.impulso_salto**2) * 0.5
				self.impulso_salto -= 1
			else:
				self.ha_saltado = False
				self.impulso_salto = 10
		else:
			#Permite moverse arriba y abajo sin saltar
			if k[ar] and self.y > self.velocidad:
				self.y -= self.velocidad

			if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
				self.y += self.velocidad
			#Reconoce el salto
			if k[salta]:
				self.ha_saltado = True
				#Controles de animación
				self.va_izquierda = False
				self.va_derecha = False
				self.contador_pasos = 0
		

		

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
		heroe.se_mueve_segun(teclas,pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE)
		repintar_cuadro_juego()
# Termina el juego y finaliza los elementos de pygame
pygame.quit()
