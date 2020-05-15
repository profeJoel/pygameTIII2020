import pygame

pygame.init()
ventana_x = 1200
ventana_y = 700
ventana = pygame.display.set_mode((ventana_x,ventana_y))

pygame.display.set_caption("MI PRIMER JUEGO")

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

	if keys[pygame.K_LEFT]:
		x -= velocidad

	if keys[pygame.K_RIGHT]:
		x += velocidad

	if keys[pygame.K_UP]:
		y -= velocidad

	if keys[pygame.K_DOWN]:
		y += velocidad


    
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



	ventana.fill((0,0,0))
	
	pygame.draw.circle(ventana, (R,G,B), (x,y), radio)
	
	pygame.display.update()


pygame.quit()