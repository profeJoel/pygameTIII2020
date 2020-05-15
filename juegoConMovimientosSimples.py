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