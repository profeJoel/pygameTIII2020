import pygame
from pygame.locals import *

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))
pygame.display.set_caption("MI PRIMER JUEGO")
reloj = pygame.time.Clock()

#incluir en clase proyectil
sonidoBala = pygame.mixer.Sound('snd/bullet.wav')
sonidoGolpe = pygame.mixer.Sound('snd/hit.wav')

# es necesario un standar de carga
class personaje(object):

	def __init__(self, x, y, ancho, alto, fuente, fin):
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
		self.fin = fin
		self.camino = [self.x, self.fin]
		self.zonaImpacto = (self.x + 15, self.y + 2, 30, 55)
		self.salud = 10
		self.esVisible = True
		fuente += "/"
		self.caminaIzquierda = [pygame.image.load("img/"+fuente+"L1.png"),pygame.image.load("img/"+fuente+"L2.png"),pygame.image.load("img/"+fuente+"L3.png"),pygame.image.load("img/"+fuente+"L4.png"),pygame.image.load("img/"+fuente+"L5.png"),pygame.image.load("img/"+fuente+"L6.png"),pygame.image.load("img/"+fuente+"L7.png"),pygame.image.load("img/"+fuente+"L8.png"),pygame.image.load("img/"+fuente+"L9.png")]
		self.caminaDerecha = [pygame.image.load("img/"+fuente+"R1.png"),pygame.image.load("img/"+fuente+"R2.png"),pygame.image.load("img/"+fuente+"R3.png"),pygame.image.load("img/"+fuente+"R4.png"),pygame.image.load("img/"+fuente+"R5.png"),pygame.image.load("img/"+fuente+"R6.png"),pygame.image.load("img/"+fuente+"R7.png"),pygame.image.load("img/"+fuente+"R8.png"),pygame.image.load("img/"+fuente+"R9.png")]
		self.quieto = pygame.image.load("img/"+fuente+"standing.png")

	def dibujar(self, cuadro):
		if self.contadorPasos + 1 > 27:
			self.contadorPasos = 0

		if self.esVisible:
			if self.izquierda:
				cuadro.blit(self.caminaIzquierda[self.contadorPasos//3],(self.x,self.y))
				self.contadorPasos += 1
			elif self.derecha:
				cuadro.blit(self.caminaDerecha[self.contadorPasos//3],(self.x,self.y))
				self.contadorPasos += 1
			else:
				if self.derecha:
					cuadro.blit(self.caminaDerecha[0],(self.x,self.y))
				elif self.izquierda:
					cuadro.blit(self.caminaIzquierda[0],(self.x,self.y))
				else:
					cuadro.blit(self.quieto, (self.x,self.y))
			self.zonaImpacto = (self.x + 15, self.y + 10, 30, 50)
			#Crear clase barra de vida
			pygame.draw.rect(cuadro, (255,0,0), (self.zonaImpacto[0], self.zonaImpacto[1] - 20, 50, 10))
			pygame.draw.rect(cuadro, (0,128,0), (self.zonaImpacto[0], self.zonaImpacto[1] - 20, 50 - (5 * (10 - self.salud)), 10))
			#En caso de querer visualizar el hitbox, descomentar la siguiente linea
			#pygame.draw.rect(cuadro, (255,0,0), self.zonaImpacto, 2)
		else:
			if self.zonaImpacto[0] != -1:
				texto = pygame.font.SysFont('comicsans',100)
				marcador = texto.render('GANASTE!', 1, (255,0,0))
				cuadro.blit(marcador, (250 - (marcador.get_width()/2),200))
				pygame.display.update()
				pygame.time.delay(2000)
			self.zonaImpacto = (-1, -1, -1, -1)


	def impactarFinal(self,cuadro):
		self.haSaltado = False
		self.impulsoSalto = 10
		self.x = 100
		self.y = 410
		self.contadorPasos = 0
		'''
		texto = pygame.font.SysFont('comicsans',100)
		marcador = texto.render('-5', 1, (255,0,0))
		cuadro.blit(marcador, (250 - (marcador.get_width()/2),200))
		pygame.display.update()
		'''
		pygame.time.delay(2000)

	def impactar(self, cuadro):
		if self.salud > 0:
			self.salud -= 1
		else:
			self.esVisible = False
			del(self)

		'''
		texto = pygame.font.SysFont('comicsans',100)
		marcador = texto.render('-1', 1, (255,0,0))
		cuadro.blit(marcador, (250 - (marcador.get_width()/2),200))
		pygame.display.update()
		'''
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

	def mover_solo(self,cuadro, nivel):
		if self.velocidad > 0:
			if self.x + self.velocidad < self.camino[1]:
				self.x += self.velocidad * nivel 
				self.derecha = True
				self.izquierda = False
			else:
				self.velocidad = self.velocidad * -1
				self.contadorPasos = 0
		else:
			if self.x - self.velocidad > self.camino[0]:
				self.x += self.velocidad * nivel 
				self.izquierda = True
				self.derecha = False
			else:
				self.velocidad = self.velocidad * -1
				self.contadorPasos = 0

	def meHaTocao(self, tocador):
		R1_ab=self.zonaImpacto[1] + self.zonaImpacto[3]
		R1_ar=self.zonaImpacto[1]
		R1_iz=self.zonaImpacto[0]
		R1_de=self.zonaImpacto[0] + self.zonaImpacto[2]
		R2_ab=tocador.zonaImpacto[1] + tocador.zonaImpacto[3]
		R2_ar=tocador.zonaImpacto[1]
		R2_iz=tocador.zonaImpacto[0]
		R2_de=tocador.zonaImpacto[0] + tocador.zonaImpacto[2]

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
		self.zonaImpacto = (self.x-self.radio, self.y-self.radio, self.radio*2, self.radio*2)

	def dibujar(self, cuadro):
		self.zonaImpacto = (self.x-self.radio, self.y-self.radio, self.radio*2, self.radio*2)
		pygame.draw.circle(cuadro, self.color, (self.x, self.y), self.radio)
		#En caso de querer visualizar el hitbos, descomentar la siguiente linea
		#pygame.draw.rect(cuadro, (255,0,0), self.zonaImpacto, 2)

def rePintarCuadroJuego():
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

def subirNivel():
	global nivel
	global nivel_maximo
	global villano
	global musica
	global ventana
	global run
	global gana
	
	nivel += 1#Marca subida de nivel
	#Texto de subida de nivel
	texto = pygame.font.SysFont('comicsans',100)
	marcador = texto.render('GANASTE!', 1, (255,0,0))
	ventana.blit(marcador, (250 - (marcador.get_width()/2),200))
	pygame.display.update()
	pygame.time.delay(2000)
	#Se verifica si paso el ultimo nivel
	#En caso de pasar el ultimo nivel, gana el juego y termina el ciclo del juego (run)
	if nivel >	 nivel_maximo:
		pygame.mixer.music.stop()
		gana = True
		run = False
	#En caso de pasar un nivel intermedio, se actualiza el villano y la musica de acuerdo al nuevo nivel
	else:
		villano = villanos[nivel]
		#ver si es necesaria la consulta... observacion inicial NO SIRVE xd
		#if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
		musica = pygame.mixer.music.load(ruta_musica[nivel])
		pygame.mixer.music.play(-1)

repetir = True #Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:
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
	musica = pygame.mixer.music.load(ruta_musica[nivel])
	pygame.mixer.music.play(-1)

	texto_puntos = pygame.font.SysFont('comicsans', 30, True)
	texto_nivel = pygame.font.SysFont('comicsans', 30, True)
	texto_intro = pygame.font.SysFont('console', 30, True)
	texto_resultado = pygame.font.SysFont('console', 80, True)

	intro = True
	gana = False
	mono = personaje(50,150,64,64,"heroe",700)

	while intro:
		reloj.tick(27)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		ventana.fill((0,0,0))
		titulo = texto_intro.render('MI PRIMER JUEGO', 1, (255,0,0))
		mono.mover_solo(ventana, 2)
		instrucciones = texto_intro.render('Presione ENTER para continuar...', 1, (255,255,255))
		ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
		ventana.blit(instrucciones, ((ventana_x//2)-instrucciones.get_width()//2, 300))

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN]:
			intro=False
			run = True


		mono.dibujar(ventana)
		pygame.display.update();

	while run:
		reloj.tick(27)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		#contacto directo con villano
		if villano.esVisible:
			if heroe.meHaTocao(villano):
				heroe.impactarFinal(ventana)
				puntaje -= 5
				heroe.salud -= 5

		if tanda_disparos > 0:
			tanda_disparos += 1
		if tanda_disparos > 3:
			tanda_disparos = 0

		#contacto de proyectil con el villano
		for bala in balas:
			if villano.meHaTocao(bala):
				sonidoGolpe.play()
				villano.impactar(ventana)
				puntaje += 1
				balas.pop(balas.index(bala))

			# movimiento de la bala
			if bala.x < ventana_x and bala.x > 0:
				bala.x += bala.velocidad
			else:
				balas.pop(balas.index(bala))

		keys = pygame.key.get_pressed()

		# capturar evento del disparo
		if keys[pygame.K_x] and tanda_disparos == 0:
			if heroe.izquierda:
				direccion = -1
			elif heroe.derecha:
				direccion = 1
			else:
				direccion = 0

			if len(balas) < 5: # balas en pantalla
				balas.append(proyectil(round(heroe.x + heroe.ancho // 2), round(heroe.y + heroe.alto // 2), 6, (0,0,0), direccion))
				sonidoBala.play()
			tanda_disparos = 1


		heroe.capturar_movimiento(keys, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE)

		#villano.capturar_movimiento(keys, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_x)
		villano.mover_solo(ventana, nivel)

		# Consulta para saber si se sube de nivel
		if villano.salud <= 0:
			subirNivel()
		if heroe.salud <= 0:
			run = False

		rePintarCuadroJuego()
		
	final = True
	while final:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
		ventana.fill((0,0,0))
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

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RETURN]:
			repetir=False
			final=False

		if keys[pygame.K_r]:
			repetir=True
			final=False

			del(heroe)
			del(villano)



pygame.quit()