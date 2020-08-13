import pygame
from pygame.locals import *

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x, ventana_y))
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
        self.camina_izquierda = [pygame.image.load("img/"+fuente+"L1.png"), pygame.image.load("img/"+fuente+"L2.png"), pygame.image.load("img/"+fuente+"L3.png"), pygame.image.load("img/"+fuente+"L4.png"), pygame.image.load(
            "img/"+fuente+"L5.png"), pygame.image.load("img/"+fuente+"L6.png"), pygame.image.load("img/"+fuente+"L7.png"), pygame.image.load("img/"+fuente+"L8.png"), pygame.image.load("img/"+fuente+"L9.png")]
        self.camina_derecha = [pygame.image.load("img/"+fuente+"R1.png"), pygame.image.load("img/"+fuente+"R2.png"), pygame.image.load("img/"+fuente+"R3.png"), pygame.image.load("img/"+fuente+"R4.png"), pygame.image.load(
            "img/"+fuente+"R5.png"), pygame.image.load("img/"+fuente+"R6.png"), pygame.image.load("img/"+fuente+"R7.png"), pygame.image.load("img/"+fuente+"R8.png"), pygame.image.load("img/"+fuente+"R9.png")]
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
            cuadro.blit(self.camina_izquierda[self.contador_pasos//3], (self.x, self.y))
            self.contador_pasos += 1
        elif self.va_derecha:
            cuadro.blit(self.camina_derecha[self.contador_pasos//3], (self.x, self.y))
            self.contador_pasos += 1
        else:
            cuadro.blit(self.quieto, (self.x, self.y))

        #Dibujar hitbox
        self.zona_impacto = (self.x + 15, self.y + 10, 30, 50)
        #En caso de querer visualizar el hitbox, descomentar la siguiente linea
        #pygame.draw.rect(cuadro, (255,0,0), self.zona_impacto, 2)

        #Crear clase barra de vida
        pygame.draw.rect(cuadro, (255, 0, 0),
                         (self.zona_impacto[0], self.zona_impacto[1] - 20, 50, 10))
        pygame.draw.rect(cuadro, (0, 128, 0),
                         (self.zona_impacto[0], self.zona_impacto[1] - 20, 50 - (5 * (10 - self.salud)), 10))

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

    def se_mueve_solo(self, nivel):
        if self.velocidad > 0:
            if self.x + self.velocidad < self.camino[1]:
                self.x += self.velocidad * nivel
                self.va_derecha = True
                self.va_izquierda = False
            else:
                self.velocidad = self.velocidad * -1
                self.contador_pasos = 0
        else:
            if self.x - self.velocidad > self.camino[0]:
                self.x += self.velocidad * nivel
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

######################################################################################################################
#Clase Proyectil
# Modificada para aceptar disparo guiado por el mouse
class proyectil(object):
    def __init__(self, x, y, radio, color, destino):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.destino = destino
        # se calcula la PENDIENTE
        if self.destino[0] == self.x:
            self.m = None
        else:
            self.m = (destino[1] - y) / (destino[0] - x)
        # se almacena el valor del punto original
        self.x0 = self.x
        self.y0 = self.y
        # se establece una rapidez -> si deseas modificar la velocidad, modifica esta variable en su lugar
        self.rapidez = 20
        # se calcula la velocidad proporcionalmente para que se avanzara siempre en la misma rapidez
        self.velocidad = (self.rapidez * (destino[0] - x)) / (((destino[1] - y)**2 + (destino[0] - x)**2)**(0.5))
        self.zona_impacto = (self.x - self.radio, self.y - self.radio, self.radio*2, self.radio*2)

    def dibujar(self, cuadro):
        self.zona_impacto = (self.x - self.radio, self.y - self.radio, self.radio*2, self.radio*2)
        pygame.draw.circle(cuadro, self.color, (self.x, self.y), self.radio)

    # funcion para realizar el movimiento del disparo en el eje x e y
    def se_mueve(self):
        # caso para los movimientos verticales
        if self.m == None:
            # caso si se dispara hacia arriba
            if self.destino[1] < self.y0:
                self.y -= self.rapidez
            # caso si se dispara hacia abajo
            else:
                self.y += self.rapidez
        # caso para el resto de movimientos
        else:
            # se crea nueva x 
            self.x += self.velocidad
            # se evalua la nueva y usando la ecuación de la recta correspondiente
            self.y = self.m * (self.x - self.x0) + self.y0

    #Bala impacta a un personaje
    def impacta_a(self, alguien):
        if alguien.salud > 0:
            alguien.salud -= 1
        else:
            #alguien.es_visible = False
            del(alguien)

######################################################################################################################




#Función para repintar el cuadro de juego
def repintar_cuadro_juego():
    #Dibujar fondo del nivel
    if nivel <= nivel_maximo:
        ventana.blit(imagen_fondo[nivel], (0, 0))
    else:
        ventana.fill((0, 0, 0))
    #Dibujar Héroe
    heroe.dibujar(ventana)
    #Dibujar Villano
    villano.dibujar(ventana)
    #Dibujar Balas
    for bala in balas:
        bala.dibujar(ventana)
    #Crear textos del nivel
    puntos = texto_puntos.render('Puntaje: ' + str(puntaje), 1, (0, 0, 0))
    nivel_actual = texto_nivel.render('Nivel: ' + str(nivel), 1, (0, 0, 0))
    #Dibujar textos del nivel
    ventana.blit(puntos, (350, 10))
    ventana.blit(nivel_actual, (350, 30))
    #Se refresca la imagen
    pygame.display.update()

#Subir de nivel


def subir_nivel():
    global nivel
    global nivel_maximo
    global villano
    global musica_fondo
    global ventana
    global esta_jugando
    global gana

    nivel += 1  # Marca subida de nivel
    pygame.display.update()
    pygame.time.delay(2000)
    #Se verifica si paso el ultimo nivel
    #En caso de pasar el ultimo nivel, gana el juego y termina el ciclo del juego (esta_jugando)
    if nivel > nivel_maximo:
        pygame.mixer.music.stop()
        esta_jugando = False
        gana = True
    #En caso de pasar un nivel intermedio, se actualiza el villano y la musica de acuerdo al nuevo nivel
    else:
        villano = villanos[nivel]
        pygame.mixer.music.stop()
        musica_fondo = pygame.mixer.music.load(ruta_musica[nivel])
        pygame.mixer.music.play(-1)

# Inicio Funcion principal


repetir = True  # Variable que controla la repeticion del juego completo con todas sus pantallas
#Ciclo de repeticion de todo el juego
while repetir:

    # Inicializacion de elementos del juego
    nivel = 0
    nivel_maximo = 3
    imagen_fondo = [pygame.image.load('img/bg0.jpg'), pygame.image.load(
        'img/bg.jpg'), pygame.image.load('img/bg1.jpg'), pygame.image.load('img/bg2.jpg')]
    ruta_musica = ["snd/dubstep.mp3", "snd/moose.mp3",
                "snd/evolution.mp3", "snd/epic.mp3"]
    musica_fondo = pygame.mixer.music.load(ruta_musica[nivel])
    #pygame.mixer.music.play(-1)
    puntaje = 0
    texto_puntos = pygame.font.SysFont('comicsans', 30, True)
    texto_nivel = pygame.font.SysFont('comicsans', 30, True)
    texto_intro = pygame.font.SysFont('console', 30, True)
    texto_resultado = pygame.font.SysFont('console', 80, True)
    esta_en_intro = True
    gana = False
    personaje_intro = personaje(50, 150, "heroe", 700)

    #Creación Personaje Héroe
    heroe = personaje(int(ventana_x/2), int(ventana_y/2),
                      "heroe", ventana_x)  # Agregar límite
    villanos = [personaje(10, ventana_y - 100, "villano", 800), personaje(10, ventana_y - 100, "villano", 800),
             personaje(10, ventana_y - 100, "villano", 800), personaje(10, ventana_y - 100, "villano", 800)]
    villano = villanos[nivel]

    #Variables Balas
    tanda_disparos = 0
    balas = []
    sonido_bala = pygame.mixer.Sound('snd/bullet.wav')
    sonido_golpe = pygame.mixer.Sound('snd/hit.wav')

    # Seccion de intro
    while esta_en_intro:
        # control de velocidad del juego
        reloj.tick(27)
        # evento de boton de cierre de ventana
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

        ventana.fill((0, 0, 0))  # pinta el fondo de negro
        titulo = texto_intro.render('MI PRIMER JUEGO', 1, (255, 0, 0))
        personaje_intro.se_mueve_solo(2)
        instrucciones = texto_intro.render(
            'Presione ENTER para continuar...', 1, (255, 255, 255))
        ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
        ventana.blit(instrucciones, ((ventana_x//2) -
                               instrucciones.get_width()//2, 300))

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_RETURN]:
            esta_en_intro = False
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

        teclas = pygame.key.get_pressed()
        heroe.se_mueve_segun(teclas, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE)
        villano.se_mueve_solo(nivel)
        #Verificar si choca heroe con villano
        if heroe.se_encuentra_con(villano):
            heroe.es_golpeado()
            puntaje -= 5

        # Manejo de los disparos
        if tanda_disparos > 0:
            tanda_disparos += 1
        if tanda_disparos > 3:
            tanda_disparos = 0
            
        ######################################################################################################################
        #Captura de Mouse
        maus = pygame.mouse.get_pressed()

        #contacto de proyectil con el villano
        for bala in balas:
            if villano.se_encuentra_con(bala):
                sonido_golpe.play()  # al momento de impactar en el villano
                bala.impacta_a(villano)
                puntaje += 1
                balas.pop(balas.index(bala))  # se elimina la bala del impacto

            # movimiento de la bala dentro de los limites de la ventana
            if bala.x < ventana_x and bala.x > 0 and bala.y < ventana_y and bala.y > 0:
                bala.se_mueve() # se lanza la funcion de movimiento del disparo
            else:
                balas.pop(balas.index(bala))  # se elimina la bala fuera de la ventana

        # capturar evento del disparo con el click (click izquierdo)
        if maus[0] and tanda_disparos == 0:
            # se captura la posicion (x,y) del mouse
            destino = pygame.mouse.get_pos()

            if len(balas) < 5:  # balas en pantalla
                balas.append(proyectil(round(heroe.x + heroe.ancho // 2), round(heroe.y + heroe.alto // 2), 6, (0, 0, 0), destino))
            sonido_bala.play()  # al momento de disparar
            tanda_disparos = 1
        ######################################################################################################################

        # Consulta para saber si se sube de nivel
        if villano.salud <= 0:
            subir_nivel()
        #Consulta para saber si perdimos
        if heroe.salud <= 0:
            esta_jugando = False
        repintar_cuadro_juego()

    # Seccion de pantalla final
    final = True
    while final:
        # evento de boton de cierre de ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        ventana.fill((0, 0, 0))  # pinta el fondo de negro
        titulo = texto_intro.render('JUEGO TERMINADO', 1, (255, 0, 0))
        if gana:
            resultado = texto_resultado.render('HAS GANADO! UwU', 1, (255, 0, 0))
        else:
            resultado = texto_resultado.render('HAS PERDIDO! :(', 1, (255, 0, 0))
        pts = texto_intro.render('Puntaje Total: '+str(puntaje), 1, (255, 255, 255))
        instrucciones = texto_intro.render(
            'Presione ENTER para cerrar...', 1, (255, 255, 255))
        reintentar = texto_intro.render(
            'Presione R para volver al juego...', 1, (255, 255, 255))
        ventana.blit(titulo, ((ventana_x//2)-titulo.get_width()//2, 10))
        ventana.blit(resultado, ((ventana_x//2)-resultado.get_width()//2, 200))
        ventana.blit(pts, ((ventana_x//2)-titulo.get_width()//2, 100))
        ventana.blit(instrucciones, ((ventana_x//2) -
                               instrucciones.get_width()//2, 300))
        ventana.blit(reintentar, ((ventana_x//2)-reintentar.get_width()//2, 350))
        pygame.display.update()

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_RETURN]:
            repetir = False
            final = False

        if tecla[pygame.K_r]:
            repetir = True
            final = False
            # se asegura de eliminar los objetos de cada personaje
            del(heroe)
            del(villano)

# Termina el juego y finaliza los elementos de pygame
pygame.quit()
