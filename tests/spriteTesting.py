'''
********************************************
File: spriteTesting.py
Author: Luke Burks
Date: November 2017


Testing game sprites
********************************************
'''
from __future__ import division

__author__ = "Luke Burks"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Luke Burks"
__email__ = "clburks9@gmail.com"
__status__ = "Development"



import sys, pygame
import inspect
import numpy as np; 

pygame.init()

class Ball:

	def __init__(self,surf):
		
		self.img = surf.copy();
		self.img = pygame.transform.scale(self.img,(10,10));
		self.rect= self.img.get_bounding_rect()
		self.rect = self.rect.move([np.random.randint(100,800),np.random.randint(100,700)]);

		self.allGoals = [[100,100],[400,100],[400,600],[800,100],[700,700]];
		self.red = True; 
		self.setNewGoal(); 
		
		

	def goalDist(self):
		return np.sqrt((self.rect.center[0]-self.goal[0])**2 + (self.rect.center[1]-self.goal[1])**2)

	def reColor(self,red,green,blue):
		arr = pygame.surfarray.pixels3d(self.img); 
		#print(arr); 
		arr[:,:,0] = red; 
		arr[:,:,1] = green; 
		arr[:,:,2] = blue; 

	def setNewGoal(self):
		self.goal = self.allGoals[np.random.randint(0,len(self.allGoals))]; 

		self.speed = [self.goal[0]-self.rect.center[0],self.goal[1]-self.rect.center[1]]; 
		suma = abs(self.speed[0])+abs(self.speed[1]); 
		self.speed[0] = self.speed[0]*10/suma; 
		self.speed[1] = self.speed[1]*10/suma; 

		if(self.red):
			self.red = False;
			self.img.convert_alpha(); 
			self.reColor(0,255,0); 
		else:
			self.red = True;
			self.img.convert_alpha(); 
			self.reColor(255,0,0); 

		#self.img = pygame.transform.rotate(self.img,np.degrees(np.arctan2(self.speed[0],self.speed[1])));


	def update(self,width,height):
		
		if(self.goalDist()<75):
			self.setNewGoal(); 

		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > width:
		    self.speed[0] = -self.speed[0]
		    self.img = pygame.transform.flip(self.img,True,False);
		if self.rect.top < 0 or self.rect.bottom > height:
		    self.speed[1] = -self.speed[1]
		    self.img = pygame.transform.flip(self.img,False,True);





size = width, height = 900, 700
white = 255, 255, 255
fps = 30; 

screen = pygame.display.set_mode(size)

primeAnt = pygame.image.load("ant.png"); 
allAnts = []; 
for i in range(0,40):
	allAnts.append(Ball(primeAnt)); 


print("Ants loaded");
clock = pygame.time.Clock();

#screen.fill(white)
while 1: 
	for event in pygame.event.get():
	    if event.type == pygame.QUIT: sys.exit()

	for ant in allAnts:
		ant.update(width,height)

	screen.fill(white)
	for ant in allAnts:
		screen.blit(ant.img, ant.rect)
		

	
	clock.tick(fps);
	pygame.display.flip()





