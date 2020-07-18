import pygame
from pygame.locals import *

pygame.init() # HOla Cris Holi :D
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("MI PRIMER JUEGO")
reloj = pygame.time.Clock()

#incluir en clase proyectil
sonido_bala = pygame.mixer.Sound('snd/bullet.wav')
sonido_golpe = pygame.mixer.Sound('snd/hit.wav')

# es necesario un standar de carga
class personaje(object):

	def __init__(self, x, y, ancho, alto, fuente, fin):
		self.x = x
		self.y = y
		self.ancho = ancho
		self.alto = alto
		self.velocidad = 5
		self.ha_saltado = False
		self.impulso_salto = 10
		self.va_izquierda = False
		self.va_derecha = False
		self.contador_pasos = 0
		self.fin = fin
		self.camino = [self.x, self.fin]
		self.zona_impacto = (self.x + 15, self.y + 2, 30, 55)
		self.salud = 10
		self.es_visible = True
		fuente += "/"
		self.camina_izquierda = [pygame.image.load("img/"+fuente+"L1.png"),pygame.image.load("img/"+fuente+"L2.png"),pygame.image.load("img/"+fuente+"L3.png"),pygame.image.load("img/"+fuente+"L4.png"),pygame.image.load("img/"+fuente+"L5.png"),pygame.image.load("img/"+fuente+"L6.png"),pygame.image.load("img/"+fuente+"L7.png"),pygame.image.load("img/"+fuente+"L8.png"),pygame.image.load("img/"+fuente+"L9.png")]
		self.camina_derecha = [pygame.image.load("img/"+fuente+"R1.png"),pygame.image.load("img/"+fuente+"R2.png"),pygame.image.load("img/"+fuente+"R3.png"),pygame.image.load("img/"+fuente+"R4.png"),pygame.image.load("img/"+fuente+"R5.png"),pygame.image.load("img/"+fuente+"R6.png"),pygame.image.load("img/"+fuente+"R7.png"),pygame.image.load("img/"+fuente+"R8.png"),pygame.image.load("img/"+fuente+"R9.png")]
		self.quieto = pygame.image.load("img/"+fuente+"standing.png")

	def dibujar(self, cuadro):
		if self.contador_pasos + 1 > 27:
			self.contador_pasos = 0

		if self.es_visible:
			if self.izquierda:
				cuadro.blit(self.camina_izquierda[self.contador_pasos//3],(self.x,self.y))
				self.contador_pasos += 1
			elif self.derecha:
				cuadro.blit(self.camina_derecha[self.contador_pasos//3],(self.x,self.y))
				self.contador_pasos += 1
			else:
				if self.derecha:
					cuadro.blit(self.camina_derecha[0],(self.x,self.y))
				elif self.izquierda:
					cuadro.blit(self.camina_izquierda[0],(self.x,self.y))
				else:
					cuadro.blit(self.quieto, (self.x,self.y))
			self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)
			#Crear clase barra de vida
			pygame.draw.rect(cuadro, (255,0,0), (self.zona_impacto[0], self.zona_impacto[1] - 20, 50, 10))
			pygame.draw.rect(cuadro, (0,128,0), (self.zona_impacto[0], self.zona_impacto[1] - 20, 50 - (5 * (10 - self.salud)), 10))
			#En caso de querer visualizar el hitbox, descomentar la siguiente linea
			#pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)
		else:
			if self.zona_impacto[0] != -1:
				texto = pygame.font.SysFont('comicsans',100)
				marcador = texto.render('GANASTE!', 1, (255,0,0))
				cuadro.blit(marcador, (250 - (marcador.get_width()/2),200))
				pygame.display.update()
				pygame.time.delay(2000)
			self.zona_impacto = (-1, -1, -1, -1)

	def es_golpeado(self, cuadro):
		self.ha_saltado = False
		self.impulso_salto = 10
		self.x = 100
		self.y = 410
		self.contador_pasos = 0
		pygame.time.delay(2000)

	def siente_impacto(self, cuadro):
		if self.salud > 0:
			self.salud -= 1
		else:
			self.es_visible = False
			del(self)

	def captura_movimiento(self, k, iz, de, ar, ab, salta):
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
			self.contador_pasos = 0


		if not self.ha_saltado:
			if k[ar] and self.y > self.velocidad:
				self.y -= self.velocidad

			if k[ab] and self.y < ventana_y - self.alto - self.velocidad:
				self.y += self.velocidad

			if k[salta]:
				self.ha_saltado = True
				self.izquierda = False
				self.derecha = False
				self.contador_pasos = 0
		else:
			if self.impulso_salto >= -10:
				if self.impulso_salto < 0:
					self.y -= (self.impulso_salto**2) * 0.5 * -1
				else:
					self.y -= (self.impulso_salto**2) * 0.5
				self.impulso_salto -= 1
			else:
				self.ha_saltado = False
				self.impulso_salto = 10

	def se_mueve_solo(self, cuadro, nivel):
		if self.velocidad > 0:
			if self.x + self.velocidad < self.camino[1]:
				self.x += self.velocidad * nivel 
				self.derecha = True
				self.izquierda = False
			else:
				self.velocidad = self.velocidad * -1
				self.contador_pasos = 0
		else:
			if self.x - self.velocidad > self.camino[0]:
				self.x += self.velocidad * nivel 
				self.izquierda = True
				self.derecha = False
			else:
				self.velocidad = self.velocidad * -1
				self.contador_pasos = 0

	def se_encuentra_con(self, tocador):
		R1_ab=self.zona_impacto[1] + self.zona_impacto[3]
		R1_ar=self.zona_impacto[1]
		R1_iz=self.zona_impacto[0]
		R1_de=self.zona_impacto[0] + self.zona_impacto[2]
		R2_ab=tocador.zona_impacto[1] + tocador.zona_impacto[3]
		R2_ar=tocador.zona_impacto[1]
		R2_iz=tocador.zona_impacto[0]
		R2_de=tocador.zona_impacto[0] + tocador.zona_impacto[2]

		return R1_de > R2_iz and R1_iz < R2_de and R1_ar < R2_ab and R1_ab > R2_ar

	def __del__(self):
		pass

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
		#En caso de querer visualizar el hitbos, descomentar la siguiente linea
		#pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)

def repintar_cuadro_juego():
	#Dibujar fondo del nivel
	if nivel <= nivel_maximo:
		ventana.blit(imagen_fondo[nivel],(0,0))
	else:
		ventana.fill((0,0,0))
	#Crear textos del nivel
	puntos = texto_puntos.render('Puntaje: ' + str(puntaje), 1, (0,0,0))
	nivel_actual = texto_nivel.render('Nivel: ' + str(nivel), 1, (0,0,0))
	#Dibujar textos del nivel
	ventana.blit(puntos, (350, 10))
	ventana.blit(nivel_actual, (350, 30))
	#Dibujar personajes
	heroe.dibujar(ventana)	
	villano.dibujar(ventana)
	#Dibujar Balas
	for bala in balas:
		bala.dibujar(ventana)
	pygame.display.update()

def subir_nivel():
	global nivel
	global nivel_maximo
	global villano
	global musica_fondo
	global ventana
	global esta_jugando
	global gana
	
	nivel += 1#Marca subida de nivel
	#Texto de subida de nivel
	texto = pygame.font.SysFont('comicsans',100)
	marcador = texto.render('GANASTE!', 1, (255,0,0))
	ventana.blit(marcador, (250 - (marcador.get_width()/2),200))
	pygame.display.update()
	pygame.time.delay(2000)
	#Se verifica si paso el ultimo nivel
	#En caso de pasar el ultimo nivel, gana el juego y termina el ciclo del juego (esta_jugando)
	if nivel >	 nivel_maximo:
		pygame.mixer.music.stop()
		gana = True
		esta_jugando = False
	#En caso de pasar un nivel intermedio, se actualiza el villano y la musica de acuerdo al nuevo nivel
	else:
		villano = villanos[nivel]
		#ver si es necesaria la consulta... observacion inicial NO SIRVE xd
		#if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
		musica_fondo = pygame.mixer.music.load(ruta_musica[nivel])
		pygame.mixer.music.play(-1)

# Inicio Funcion principal

repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:

	# Inicializacion de elementos del juego
	tanda_disparos = 0
	balas = []
	puntaje = 0

	nivel = 0
	nivel_maximo = 3

	heroe = personaje(int(ventana_x/2),int(ventana_y/2),64,64,"heroe",800)
	villanos = [personaje(10,ventana_y - 100,64,64,"villano",800), personaje(10,ventana_y - 100,64,64,"villano",800), personaje(10,ventana_y - 100,64,64,"villano",800), personaje(10,ventana_y - 100,64,64,"villano",800)]
	villano = villanos[nivel]

	imagen_fondo = [pygame.image.load('img/bg0.jpg'), pygame.image.load('img/bg.jpg'), pygame.image.load('img/bg1.jpg'), pygame.image.load('img/bg2.jpg')]
	ruta_musica = ["snd/dubstep.mp3","snd/moose.mp3","snd/evolution.mp3","snd/epic.mp3"]
	musica_fondo = pygame.mixer.music.load(ruta_musica[nivel])
	pygame.mixer.music.play(-1)

	texto_puntos = pygame.font.SysFont('comicsans', 30, True)
	texto_nivel = pygame.font.SysFont('comicsans', 30, True)
	texto_intro = pygame.font.SysFont('console', 30, True)
	texto_resultado = pygame.font.SysFont('console', 80, True)

	esta_en_intro = True
	gana = False
	personaje_intro = personaje(50,150,64,64,"heroe",700)

	# Seccion de intro
	while esta_en_intro:
		# control de velocidad del juego
		reloj.tick(27)
		# evento de boton de cierre de ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()

		ventana.fill((0,0,0)) # pinta el fondo de negro
		titulo = texto_intro.render('MI PRIMER JUEGO', 1, (255,0,0))
		personaje_intro.mover_solo(ventana, 2)
		instrucciones = texto_intro.render('Presione ENTER para continuar...', 1, (255,255,255))
		ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
		ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, 300))

		tecla = pygame.key.get_pressed()

		if tecla[pygame.K_RETURN]:
			esta_en_intro=False
			esta_jugando = True

		personaje_intro.dibujar(ventana)
		pygame.display.update()

	# Seccion de juego
	while esta_jugando:
		# control de velocidad del juego
		reloj.tick(27)
		# evento de boton de cierre de ventana
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()

		# contacto directo con villano
		if villano.es_visible:
			if heroe.se_encuentra_con(villano):
				heroe.es_golpeado(ventana)
				puntaje -= 5
				heroe.salud -= 5

		# Manejo de los disparos
		if tanda_disparos > 0:
			tanda_disparos += 1
		if tanda_disparos > 3:
			tanda_disparos = 0

		#contacto de proyectil con el villano
		for bala in balas:
			if villano.se_encuentra_con(bala):
				sonido_golpe.play() # al momento de impactar en el villano
				villano.siente_impacto(ventana)
				puntaje += 1
				balas.pop(balas.index(bala)) # se elimina la bala del impacto

			# movimiento de la bala dentro de los limites de la ventana
			if bala.x < ventana_x and bala.x > 0:
				bala.x += bala.velocidad
			else:
				balas.pop(balas.index(bala)) # se elimina la bala fuera de la ventana

		# Captura evento de teclas
		tecla = pygame.key.get_pressed()

		# capturar evento del disparo
		if tecla[pygame.K_x] and tanda_disparos == 0:
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

		heroe.captura_movimiento(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE)

		#villano.capturar_movimiento(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_x)
		villano.se_mueve_solo(ventana, nivel)

		# Consulta para saber si se sube de nivel
		if villano.salud <= 0:
			subir_nivel()
		if heroe.salud <= 0:
			esta_jugando = False
		# modifica la ventana
		repintar_cuadro_juego()
		
	# Seccion de pantalla final
	final = True
	while final:
		# evento de boton de cierre de ventana
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		ventana.fill((0,0,0)) # pinta el fondo de negro
		titulo = texto_intro.render('JUEGO TERMINADO', 1, (255,0,0))
		if gana:
			resultado = texto_resultado.render('HAS GANADO! UwU', 1, (255,0,0))
		else:
			resultado = texto_resultado.render('HAS PERDIDO! :(', 1, (255,0,0))
		pts = texto_intro.render('Puntaje Total: '+str(puntaje), 1, (255,255,255))
		instrucciones = texto_intro.render('Presione ENTER para cerrar...', 1, (255,255,255))
		reintentar = texto_intro.render('Presione R para volver al juego...', 1, (255,255,255))
		ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
		ventana.blit(resultado, ((ventana_x//2)-resultado.get_width()//2, 200))
		ventana.blit(pts,((ventana_x//2)-titulo.get_width()//2, 100))
		ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, 300))
		ventana.blit(reintentar, ((ventana_x//2)-reintentar.get_width()//2, 350))
		pygame.display.update()

		tecla = pygame.key.get_pressed()

		if tecla[pygame.K_RETURN]:
			repetir=False
			final=False

		if tecla[pygame.K_r]:
			repetir=True
			final=False
			# se asegura de eliminar los objetos de cada personaje
			del(heroe)
			del(villano)

# Termina el juego y finaliza los elementos de pygame
pygame.quit()
