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

	def __init__(self, x, y, fuente, limite):
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
		#Controles de desplazamiento automático
		self.camino = [self.x, limite]
		#Nivel de Salud
		self.salud = 10

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
		#Crear clase barra de vida
		pygame.draw.rect(cuadro, (255,0,0), (self.x+5, self.y - 20, 50, 10))
		pygame.draw.rect(cuadro, (0,128,0), (self.x+5, self.y - 20, 50 - (5 * (10 - self.salud)), 10))

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
		
	def se_mueve_solo(self):
		if self.velocidad > 0:
			if self.x + self.velocidad < self.camino[1]:
				self.x += self.velocidad 
				self.va_derecha = True
				self.va_izquierda = False
			else:
				self.velocidad = self.velocidad * -1
				self.contador_pasos = 0
		else:
			if self.x - self.velocidad > self.camino[0]:
				self.x += self.velocidad 
				self.va_izquierda = True
				self.va_derecha = False
			else:
				self.velocidad = self.velocidad * -1
				self.contador_pasos = 0
		
#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Dibujar Héroe
	heroe.dibujar(ventana)
	#Dibujar Villano
	villano.dibujar(ventana)
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
	heroe=personaje(int(ventana_x/2), int(ventana_y/2),"heroe", ventana_x)#Agregar límite
	villano=personaje(0, int(ventana_y/2),"villano",int(ventana_x/2))
	
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
		villano.se_mueve_solo()
		repintar_cuadro_juego()
# Termina el juego y finaliza los elementos de pygame
pygame.quit()
