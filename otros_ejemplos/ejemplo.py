import pygame
from pygame.locals import *

def colision(posx, posy, posw, posh, objx, objy, objw, objh):
    if(posx + posw > objx and objx + objw > posx):
        if(posy + posh > objy and objy + objh > posy):
            return 1
        else:
            return 0
    else:
         return 0


pygame.init()
ventana_a = 850
ventana_b = 480

ventana = pygame.display.set_mode((ventana_a, ventana_b))
pygame.display.set_caption ("Proyecto videojuego ")
reloj = pygame.time.Clock()




#Color Pantalla
def repintar_cuadro_juego():
    ventana.blit(imagen_fondo, (0,0))
    ventana.blit(bloq, (bloq_x, bloq_y))
    ventana.blit(bloq2, (bloq2_x, bloq2_y))
    ventana.blit(bloq3, (bloq3_x, bloq3_y))
    ventana.blit(bloq4, (bloq4_x, bloq4_y))
    ventana.blit(bloq5, (bloq5_x, bloq5_y))
    ventana.blit(bloq6, (bloq6_x, bloq6_y))
    ventana.blit(bloq7, (bloq7_x, bloq7_y))
    ventana.blit(bloq8, (bloq8_x, bloq8_y))
    ventana.blit(bloq9, (bloq9_x, bloq9_y))
    ventana.blit(bloq10, (bloq10_x, bloq10_y))
    ventana.blit(bloq11, (bloq11_x, bloq11_y))
    ventana.blit(bloq12, (bloq12_x, bloq12_y))

    #pygame.draw.rect(ventana, (255,0,0),(x1,y1,ancho1,largo1))
    #pygame.draw.rect(ventana, (130,12,85),(x2,y2,ancho2,largo2))
 
    #Dibujar personaje
    ventana.blit(imagen_personaje, (x,y))
    #Se refresca
    pygame.display.update()
 
# Inicio funcion principal
 
    #Elementos
imagen_fondo = pygame.image.load('img/fondo_original.png')
 
    #Musica
ruta_musica = 'snd/snd2.ogg'
musica_fondo = pygame.mixer.music.load(ruta_musica)
#pygame.mixer.music.play(-1)
 
    #Varibles para Figuras
x1=50
y1=50
ancho1=40
largo1=60
 
x2=500
y2=300
ancho2=80
largo2=100
 
    #Varibles de personajes
x=int(770)  #(ventana_a/2)
y=int(30)  #(ventana_b/2)
imagen_personaje = pygame.image.load('img/rat.png')
ancho=imagen_personaje.get_height()
largo=imagen_personaje.get_width()
velocidad=5

#bloques nivel 1
bloq = pygame.image.load('img/bloq1.png')
bloq_alt = bloq.get_height()
bloq_an = bloq.get_width()
bloq_x = 348
bloq_y = 0

bloq2 = pygame.image.load('img/bloq2.png')
bloq2_alt = bloq2.get_height()
bloq2_an = bloq2.get_width()
bloq2_x = 348
bloq2_y = 200

bloq3 = pygame.image.load('img/bloq3.png')
bloq3_alt = bloq3.get_height()
bloq3_an = bloq3.get_width()
bloq3_x = 200
bloq3_y = 0

bloq4 = pygame.image.load('img/bloq4.png')
bloq4_alt = bloq4.get_height()
bloq4_an = bloq4.get_width()
bloq4_x = 400
bloq4_y = 300
#bloque de incio de nivel
bloq5 = pygame.image.load('img/bloq5.png')
bloq5_alt = bloq5.get_height()
bloq5_an = bloq5.get_width()
bloq5_x = 750
bloq5_y = 0

bloq6 = pygame.image.load('img/bloq6.png')
bloq6_alt = bloq6.get_height()
bloq6_an = bloq6.get_width()
bloq6_x = 0
bloq6_y = 260
 #bloque de final de nivel
bloq7 = pygame.image.load('img/bloq7.png')
bloq7_alt = bloq7.get_height()
bloq7_an = bloq7.get_width()
bloq7_x = 0
bloq7_y = 0

bloq8 = pygame.image.load('img/bloq8.png')
bloq8_alt = bloq8.get_height()
bloq8_an = bloq8.get_width()
bloq8_x = 0
bloq8_y = 203

bloq9 = pygame.image.load('img/bloq9.png')
bloq9_alt = bloq9.get_height()
bloq9_an = bloq9.get_width()
bloq9_x = 200
bloq9_y = 400

bloq10 = pygame.image.load('img/bloq10.png')
bloq10_alt = bloq10.get_height()
bloq10_an = bloq10.get_width()
bloq10_x = 600
bloq10_y = 430

bloq11 = pygame.image.load('img/bloq11.png')
bloq11_alt = bloq11.get_height()
bloq11_an = bloq11.get_width()
bloq11_x = 647
bloq11_y = 247

bloq12 = pygame.image.load('img/bloq12.png')
bloq12_alt = bloq12.get_height()
bloq12_an = bloq12.get_width()
bloq12_x = 700
bloq12_y = 100




repetir = True #ciclo de repeticion de todo el juego 
while repetir:
 
    jugando = True
    while jugando:
     #control del juego 
        reloj.tick(27)
        #evento de boton de cierre
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
        
        #Evento(Movimientos)
        teclas=pygame.key.get_pressed()
        
        if teclas[pygame.K_LEFT] and x-velocidad > 0:
            x-=velocidad
            if colision(x, y, ancho, largo, bloq_x, bloq_y, bloq_an, bloq_alt):
                x+=velocidad
            elif colision(x, y, ancho, largo, bloq2_x, bloq2_y, bloq2_an, bloq2_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq3_x, bloq3_y, bloq3_an, bloq3_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq4_x, bloq4_y, bloq4_an, bloq4_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq6_x, bloq6_y, bloq6_an, bloq6_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq8_x, bloq8_y, bloq8_an, bloq8_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq9_x, bloq9_y, bloq9_an, bloq9_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq10_x, bloq10_y, bloq10_an, bloq10_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq11_x, bloq11_y, bloq11_an, bloq11_alt):
                x+= velocidad
            elif colision(x, y, ancho, largo, bloq12_x, bloq12_y, bloq12_an, bloq12_alt):
                x+= velocidad
        if teclas[pygame.K_RIGHT] and x+velocidad < ventana_a - ancho:
            x+=velocidad
            if colision(x, y, ancho, largo, bloq_x, bloq_y, bloq_an, bloq_alt):
                x-=velocidad
            elif colision(x, y, ancho, largo, bloq2_x, bloq2_y, bloq2_an, bloq2_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq3_x, bloq3_y, bloq3_an, bloq3_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq3_x, bloq3_y, bloq3_an, bloq3_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq4_x, bloq4_y, bloq4_an, bloq4_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq6_x, bloq6_y, bloq6_an, bloq6_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq8_x, bloq8_y, bloq8_an, bloq8_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq9_x, bloq9_y, bloq9_an, bloq9_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq10_x, bloq10_y, bloq10_an, bloq10_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq11_x, bloq11_y, bloq11_an, bloq11_alt):
                x-= velocidad
            elif colision(x, y, ancho, largo, bloq12_x, bloq12_y, bloq12_an, bloq12_alt):
                x-= velocidad
        if teclas[pygame.K_UP] and y-velocidad > 0:
            y-=velocidad
            if colision(x, y, ancho, largo, bloq_x, bloq_y, bloq_an, bloq_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq2_x, bloq2_y, bloq2_an, bloq2_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq2_x, bloq2_y, bloq2_an, bloq2_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq3_x, bloq3_y, bloq3_an, bloq3_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq4_x, bloq4_y, bloq4_an, bloq4_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq6_x, bloq6_y, bloq6_an, bloq6_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq8_x, bloq8_y, bloq8_an, bloq8_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq9_x, bloq9_y, bloq9_an, bloq9_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq10_x, bloq10_y, bloq10_an, bloq10_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq11_x, bloq11_y, bloq11_an, bloq11_alt):
                y+= velocidad
            elif colision(x, y, ancho, largo, bloq12_x, bloq12_y, bloq12_an, bloq12_alt):
                y+= velocidad
        if teclas[pygame.K_DOWN] and y+velocidad < ventana_b - largo:
            y+=velocidad
            if colision(x, y, ancho, largo, bloq_x, bloq_y, bloq_an, bloq_alt):
                y-=velocidad
            elif colision(x, y, ancho, largo, bloq2_x, bloq2_y, bloq2_an, bloq2_alt):
                y-=velocidad
            elif colision(x, y, ancho, largo, bloq2_x, bloq2_y, bloq2_an, bloq2_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq3_x, bloq3_y, bloq3_an, bloq3_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq4_x, bloq4_y, bloq4_an, bloq4_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq6_x, bloq6_y, bloq6_an, bloq6_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq8_x, bloq8_y, bloq8_an, bloq8_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq9_x, bloq9_y, bloq9_an, bloq9_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq10_x, bloq10_y, bloq10_an, bloq10_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq11_x, bloq11_y, bloq11_an, bloq11_alt):
                y-= velocidad
            elif colision(x, y, ancho, largo, bloq12_x, bloq12_y, bloq12_an, bloq12_alt):
                y-= velocidad
        repintar_cuadro_juego()
pygame.quit()
pygame.time.delay(1000)
#finalizacion del juego
