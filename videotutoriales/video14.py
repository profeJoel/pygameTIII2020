import pygame
from pygame.locals import *

pygame.init()
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
		#Hitbox
		self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)

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
			cuadro.blit(self.quieto, (self.x,self.y))
		
		#Dibujar hitbox
		self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)
		#En caso de querer visualizar el hitbox, descomentar la siguiente linea
		#pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)

		#Crear clase barra de vida
		pygame.draw.rect(cuadro, (255,0,0), (self.zona_impacto[0], self.zona_impacto[1] - 20, 50, 10))
		pygame.draw.rect(cuadro, (0,128,0), (self.zona_impacto[0], self.zona_impacto[1] - 20, 50 - (5 * (10 - self.salud)), 10))
		

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
		

	#Detección de colisiones
	def se_encuentra_con(self, alguien):
		R1_ab = self.zona_impacto[1] + self.zona_impacto[3]
		R1_ar = self.zona_impacto[1]
		R1_iz = self.zona_impacto[0]
		R1_de = self.zona_impacto[0] + self.zona_impacto[2]
		R2_ab = alguien.zona_impacto[1] + alguien.zona_impacto[3]
		R2_ar = alguien.zona_impacto[1]
		R2_iz = alguien.zona_impacto[0]
		R2_de = alguien.zona_impacto[0] + alguien.zona_impacto[2]

		return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar

	#Personaje recibe golpe de daño de parte de otro personaje
	def es_golpeado(self):
		self.ha_saltado = False
		self.impulso_salto = 10
		self.x = 100
		self.y = 410
		self.contador_pasos = 0
		self.salud -= 5
		pygame.time.delay(2000)

#Clase Proyectil
class proyectil(object):
	def __init__(self, x,y,radio,color, direccion):
		self.x = x
		self.y = y
		self.radio = radio
		self.color = color
		self.direccion = direccion
		self.velocidad = 8 * direccion
		self.zona_impacto = (self.x-self.radio, self.y-self.radio, self.radio*2, self.radio*2)

	def dibujar(self, cuadro):
		self.zona_impacto = (self.x-self.radio, self.y-self.radio, self.radio*2, self.radio*2)
		pygame.draw.circle(cuadro, self.color, (self.x, self.y), self.radio)
		#En caso de querer visualizar el hitbox, descomentar la siguiente linea
		#pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)

	#Bala impacta a un personaje
	def impacta_a(self, alguien):
		if alguien.salud > 0:
			alguien.salud -= 1
		else:
			#alguien.es_visible = False
			del(alguien)

#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	#Dibujar Héroe
	heroe.dibujar(ventana)
	#Dibujar Villano
	villano.dibujar(ventana)
	#Dibujar Balas
	for bala in balas:
		bala.dibujar(ventana)
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

	#Variables Balas
	tanda_disparos = 0
	balas = []
	sonido_bala = pygame.mixer.Sound('snd/bullet.wav')
	sonido_golpe = pygame.mixer.Sound('snd/hit.wav')
	
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
		#Verificar si choca heroe con villano
		if heroe.se_encuentra_con(villano):
			heroe.es_golpeado()
			
		# Manejo de los disparos
		if tanda_disparos > 0:
			tanda_disparos += 1
		if tanda_disparos > 3:
			tanda_disparos = 0

		#contacto de proyectil con el villano
		for bala in balas:
			if villano.se_encuentra_con(bala):
				sonido_golpe.play() # al momento de impactar en el villano
				bala.impacta_a(villano)
				balas.pop(balas.index(bala)) # se elimina la bala del impacto

			# movimiento de la bala dentro de los limites de la ventana
			if bala.x < ventana_x and bala.x > 0:
				bala.x += bala.velocidad
			else:
				balas.pop(balas.index(bala)) # se elimina la bala fuera de la ventana

		# capturar evento del disparo
		if teclas[pygame.K_x] and tanda_disparos == 0:
			if heroe.va_izquierda:
				direccion = -1
			elif heroe.va_derecha:
				direccion = 1
			else:
				direccion = 0

			if len(balas) < 5: # balas en pantalla
				balas.append(proyectil(round(heroe.x + heroe.ancho // 2), round(heroe.y + heroe.alto // 2), 6, (0,0,0), direccion))
				sonido_bala.play() # al momento de disparar
			tanda_disparos = 1
		repintar_cuadro_juego()
# Termina el juego y finaliza los elementos de pygame
pygame.quit()
