import pygame

pygame.init()
ventana_x = 850
ventana_y = 480
ventana = pygame.display.set_mode((ventana_x,ventana_y))

pygame.display.set_caption("MI PRIMER JUEGO")

imagen_fondo = pygame.image.load('img/bg.jpg')

personaje = pygame.image.load('img/standing.png')
personaje1 = pygame.image.load('img/R5E.png')


musica = pygame.mixer.music.load('img/music.mp3')
pygame.mixer.music.play(-1)


x = 50
y = 50

x = int(ventana_x/2)
y = int(ventana_y/2)

alto = 60
ancho = 40

velocidad = 5

R = 50
G = 50
B = 50
radio = 100


haSaltado = False
impulsoSalto = 12


x1 = int(ventana_x/2) + 100
y1 = int(ventana_y/2)

haSaltado1 = False
impulsoSalto1 = 12


superVerlocidad = False
temporizador = 10

run = True
while run:
	pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	'''
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		x -= vel

	if keys[pygame.K_RIGHT]:
		x+= vel

	if keys[pygame.K_UP]:
		y-= vel

	if keys[pygame.K_DOWN]:
		y+= vel

	win.fill((0,0,0))


	pygame.draw.rect(ventana, (255,255,255), (x,y,ancho,alto))
	pygame.draw.rect(ventana, (255,0,0), (x+10,y+10,ancho,alto))
	#pygame.draw.rect(ventana, (0,255,0), (500-x,500-y,ancho,alto))

	pygame.draw.ellipse(ventana, (0,255,0), (500-x,500-y,ancho,alto),10)
	pygame.display.update()
	'''

	'''
	# Captura todos los eventos posibles mediante el teclado
	keys = pygame.key.get_pressed()
    
    # Captura la ejecución de una tecla
	if keys[pygame.K_SPACE]:
		if(R<254 and G<254 and B<254):
			R = R + 2
			G = G + 2
			B = B + 2

	if keys[pygame.K_r]:
		if(R<254):
			R = R + 2

	if keys[pygame.K_g]:
		if(G<254):
			G = G + 2

	if keys[pygame.K_b]:
		if(B<254):
			B = B + 2

	pygame.draw.circle(ventana, (R,G,B), (int(ventana_x/2),int(ventana_y/2)), radio)
	
	pygame.display.update()
	'''

	keys = pygame.key.get_pressed()

	#if keys[pygame.K_LEFT] and superVerlocidad == False and x > velocidad:
	if keys[pygame.K_LEFT] and x > velocidad:
		x -= velocidad
		#superVerlocidad = True
		#temporizador = 10

	if keys[pygame.K_RIGHT] and x < ventana_x - ancho - velocidad:
		x += velocidad

	'''
	if keys[pygame.K_UP] and y > velocidad:
		y -= velocidad

	if keys[pygame.K_DOWN] and y < ventana_y - alto - velocidad:
		y += velocidad
	'''


	if not haSaltado:
		if keys[pygame.K_UP] and y > velocidad:
			y -= velocidad

		if keys[pygame.K_DOWN] and y < ventana_y - alto - velocidad:
			y += velocidad

		if keys[pygame.K_SPACE]:
			haSaltado = True
	else:
		if impulsoSalto >= -12:
			if impulsoSalto < 0:
				y -= (impulsoSalto ** 2) * 0.5 * -1
			else:
				y -= (impulsoSalto ** 2) * 0.5
			impulsoSalto -= 1 
		else:
			haSaltado = False
			impulsoSalto = 12

		'''
		if impulsoSalto >= -15:
			if impulsoSalto > 0:
				y -= (impulsoSalto ** 2) * 0.5 * -1
			else:
				y -= (impulsoSalto ** 2) * 0.5
			impulsoSalto -= 1 
		'''
		
	'''
	if keys[pygame.K_LEFT] and superVerlocidad == True and temporizador > 0 and x > velocidad*2:
		x -= velocidad * 5
		superVerlocidad = False
		temporizador = 10
	'''




    
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




	if keys[pygame.K_a] and x1 > velocidad:
		x1 -= velocidad

	if keys[pygame.K_d] and x1 < ventana_x - ancho - velocidad:
		x1 += velocidad

	if not haSaltado1:
		if keys[pygame.K_w] and y1 > velocidad:
			y1 -= velocidad

		if keys[pygame.K_s] and y1 < ventana_y - alto - velocidad:
			y1 += velocidad

		if keys[pygame.K_x]:
			haSaltado1 = True
	else:
		if impulsoSalto1 >= -12:
			if impulsoSalto1 < 0:
				y1 -= (impulsoSalto1 ** 2) * 0.5 * -1
			else:
				y1 -= (impulsoSalto1 ** 2) * 0.5
			impulsoSalto1 -= 1 
		else:
			haSaltado1 = False
			impulsoSalto1 = 12



	#ventana.fill((0,0,0))
	ventana.blit(imagen_fondo,(0,0))

	ventana.blit(personaje,(x,y))
	ventana.blit(personaje1,(x1,y1))
	#pygame.draw.rect(ventana, (R,G,B), (x,y,ancho,alto))
	#pygame.draw.circle(ventana, (R,G,B), (x,y), radio)
	
	pygame.display.update()

	temporizador -= 1

pygame.quit()