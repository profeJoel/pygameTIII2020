import pygame

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))

pygame.display.set_caption("MI PRIMER JUEGO")

imagen_fondo = pygame.image.load('img/bg.jpg')
personaje = pygame.image.load('img/standing.png')
musica = pygame.mixer.music.load('snd/music.mp3')
pygame.mixer.music.play(-1)

x = 50
y = 50

x = int(ventana_x/2)
y = int(ventana_y/2)

alto = 64
ancho = 64

velocidad = 5

R = 50
G = 50
B = 50
radio = 100

haSaltado = False
impulso = 10

run = True
while run:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	keys = pygame.key.get_pressed()
	'''
	if keys[pygame.K_LEFT] and x-radio > velocidad:
		x -= velocidad

	if keys[pygame.K_RIGHT] and x < ventana_x - radio - velocidad:
		x += velocidad

	if keys[pygame.K_UP] and y-radio > velocidad:
		y -= velocidad

	if keys[pygame.K_DOWN] and y < ventana_y - radio - velocidad:
		y += velocidad
	'''


	if keys[pygame.K_LEFT] and x > velocidad:
		x -= velocidad

	if keys[pygame.K_RIGHT] and x < ventana_x - ancho - velocidad:
		x += velocidad

	if not haSaltado:
		if keys[pygame.K_UP] and y > velocidad:
			y -= velocidad

		if keys[pygame.K_DOWN] and y < ventana_y - alto - velocidad:
			y += velocidad

		if keys[pygame.K_SPACE]:
			haSaltado = True
	else:
		if impulso >= -10:
			if impulso < 0:
				y -= (impulso**2) * 0.5 * -1
			else:
				y -= (impulso**2) * 0.5
			impulso -= 1
		else:
			haSaltado = False
			impulso = 10



    
    # Captura la ejecución de una tecla
	if keys[pygame.K_SPACE]:
		if(R<255 and G<255 and B<255):
			R = R + 5
			G = G + 5
			B = B + 5

	if keys[pygame.K_r]:
		if(R<255):
			R = R + 5

	if keys[pygame.K_g]:
		if(G<255):
			G = G + 5

	if keys[pygame.K_b]:
		if(B<255):
			B = B + 5



	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))
	
	#pygame.draw.circle(ventana, (R,G,B), (x,y), radio)
	ventana.blit(personaje,(x,y))
	#pygame.draw.rect(ventana, (R,G,B), (x,y,ancho,alto))
	
	pygame.display.update()


pygame.quit()