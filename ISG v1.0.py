import pygame, math, sys, random
import numpy as np
from random import choice
pygame.init()

#Generador de espirales infinitas
#Versión: 1.0
#Fecha de creación: 06/03/2023

#______________________________________
# !! PARÁMETROS A MODIFICAR !!
Nelement = 400				#Numero de puntos que se grafican uniendolos con lineas
Incrementoiter =0.0001		#Incremento de ángulo entre cada iteración
IncrementoR = 1				#Incremento fijo del radio entre cada punto y el siguiente
Twait= 1					#Tiempo de espera entre cada iteración
#______________________________________

# definir colores
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Yellow = (255, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)

# Color Variable
Re = 255
Gr = 255
Bl = 255
Colorvar = (Re, Gr, Bl)

# crear ventana
size = (0, 0)
screen = pygame.display.set_mode(size)
#Dar nombre e icono
pygame.display.set_caption("ISG v1.0 (Infinite Spiral Generator)")

#Datos Iniciales
IncrementoAng = 0
# los vectores de radio y ángulos se guardan como listas, inicialmente como (0, 1, 2, 3, 4...)
R = list(np.arange(0,Nelement,1))
Ang = list(np.arange(0,Nelement,1))

#Cambiamos los valores de la lista del radio por los que queremos
r=0
while r < Nelement:
	R[r] = IncrementoR*r
	r += 1


X = list(np.arange(0,Nelement,1))
Y = list(np.arange(0,Nelement,1))

colornum = 0 # 0 = Re ; 1 = Gr ; 2 = Bl
increm = 1 # 0 = Subir ; 1 = Bajar
Pausa = 1
PausaOn = 0
while True:
	# Poner color de fondo		
	screen.fill(Black)

#Hacer que el color de la espiral varie progresivamente
	#Varia si se incrementa o se dismuniye el elemento de color que se esta cambiando. en función de si se ha llegado al máximo o al mínimo
	if (Re == 0 and colornum == 0) or (Gr == 0 and colornum == 1) or (Bl == 0 and colornum == 2):
		increm =0
	elif (Re == 255 and colornum == 0) or (Gr == 255 and colornum == 1) or (Bl == 255 and colornum == 2):
		increm =1

	#Incrementa o disminuye el valor del elemento de color elegido aleatoriamente
	if colornum == 0 and Re <= 255 and Re >= 0:
		if increm == 1:
			Re -= 1
		elif increm == 0:
			Re += 1
	elif colornum == 1 and Gr <= 255 and Gr >= 0:
		if increm == 1:
			Gr -= 1
		elif increm == 0:
			Gr += 1
	elif colornum == 2 and Bl <= 255 and Bl >= 0:
		if increm == 1:
			Bl -= 1
		elif increm == 0:
			Bl += 1
	Colorvar = (Re, Gr, Bl)

	# Cambia el elemento de color a variar cuando se ha alcanzado el máximo o mínimo del que se estaba cambiando antes
	if colornum == 0 and (Re == 0 or Re == 255):
		numeros0 = [1,2]
		colornum = random.choice(numeros0)
	elif colornum == 1 and (Gr == 0 or Gr == 255):
		numeros1 = [0,2]
		colornum = random.choice(numeros1)
	elif colornum == 2 and (Bl == 0 or Bl == 255):
		numeros2 = [0,1]
		colornum = random.choice(numeros2)

	# Evita que se genere el color negro
	if Re == 0 and Gr == 0:
		numerosBlack = [0,1]
		colornum = random.choice(numerosBlack)
	elif Re == 0 and Bl == 0:
		numeros1 = [0,2]
		colornum = random.choice(numeros1)
	elif Bl == 0 and Gr == 0:
		numeros2 = [1,2]
		colornum = random.choice(numeros2)


	#Cambiamos los valores de la lista de los ángulos por los que queremos
	q=0
	while q < Nelement:
		Ang[q] = IncrementoAng*q
		q += 1


	i = 0
	for a in Ang:
		X[i]= (R[i]*math.sin(a))+770
		Y[i]= (R[i]*math.cos(a))+430
		i += 1

	z = 0
	for b in X:
		pygame.draw.line(screen, Colorvar, (X[z], Y[z]), (X[z+1], Y[z+1]),1)
		z += 1
		if z >= (Nelement-1):
			break


	
		# pygame.draw.rect(screen, Black, (x, 430, 50, 50))
	
		# pygame.draw.line(screen, Blue, (750, y), (500, y),10)

	# Actualizar pantalla
	pygame.display.flip()
	#Pausar y incrementar el ángulo.
	pygame.time.wait(Twait)
	IncrementoAng += Incrementoiter

	# Salir cuando se cierre la ventana.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() 
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				Pausa = 0
			if event.key == pygame.K_ESCAPE:
				sys.exit() 

				#Bucle de Pausa
	while Pausa == 0:
		pygame.time.wait(50)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					Pausa = 1
					pygame.time.wait(50)
				if event.key == pygame.K_ESCAPE:
					sys.exit() 
	