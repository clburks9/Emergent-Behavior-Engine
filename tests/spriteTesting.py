'''
********************************************
File: spriteTesting.py
Author: Luke Burks
Date: November 2017


Testing game sprites
********************************************
'''

import sys, pygame
import inspect
import numpy as np; 

pygame.init()

class Ball:

	def __init__(self,surf):
		self.speed = [int(np.random.randint(-5,5)), int(np.random.randint(-5,5))]
		self.img = surf.copy();
		self.img = pygame.transform.scale(self.img,(10,10));
		self.img = pygame.transform.rotate(self.img,np.degrees(int(np.arctan2(self.speed[1],self.speed[0]))));
		self.rect= self.img.get_bounding_rect()
		self.rect = self.rect.move([np.random.randint(100,800),np.random.randint(100,700)]);



size = width, height = 900, 700
speed = [np.random.randint(-3,3), np.random.randint(-3,3)]
white = 255, 255, 255

screen = pygame.display.set_mode(size)

primeAnt = pygame.image.load("ant.png"); 
allAnts = []; 
for i in range(0,500):
	allAnts.append(Ball(primeAnt)); 


print("Ants loaded");
clock = pygame.time.Clock();
  


while 1: 
	for event in pygame.event.get():
	    if event.type == pygame.QUIT: sys.exit()

	for ant in allAnts:
		ant.rect = ant.rect.move(ant.speed)
		if ant.rect.left < 0 or ant.rect.right > width:
		    ant.speed[0] = -ant.speed[0]
		    ant.img = pygame.transform.flip(ant.img,True,False);
		if ant.rect.top < 0 or ant.rect.bottom > height:
		    ant.speed[1] = -ant.speed[1]
		    ant.img = pygame.transform.flip(ant.img,False,True);

	screen.fill(white)

	for ant in allAnts:
		screen.blit(ant.img, ant.rect)

	clock.tick(60);
	pygame.display.flip()





