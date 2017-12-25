'''
********************************************
File: emergentAnts.py
Author: Luke Burks
Date: December 2017


Simulating the emergent behavior of ant
role switching. 
Inspired by: 
https://www.youtube.com/watch?v=16W7c0mb-rE
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
from AntSprites import *


def fillAntArray(primeAnt,numPer = 40):
	allAnts = []; 
	for i in range(0,numPer):
		allAnts.append(BuilderAnt(primeAnt)); 
	for i in range(0,numPer):
		allAnts.append(SoliderAnt(primeAnt)); 
	for i in range(0,numPer):
		allAnts.append(GathererAnt(primeAnt)); 
	for i in range(0,numPer):
		allAnts.append(NurseAnt(primeAnt));

	return allAnts;



def checkCollisions(allAnts):

	#update counts
	for ant1 in allAnts:
		for ant2 in allAnts:
			if(ant2.ID not in ant1.encounters and ant1.rect.colliderect(ant2.rect)):
				ant1.encounters.append(ant2.ID); 
				ant1.counts[ant2.__class__.__name__] += 1; 

	#drop oldest encounters
	totalEncounters = 50; 
	for ant1 in allAnts:
		if(len(ant1.encounters) > totalEncounters):
			ant1.encounters = ant1.encounters[-totalEncounters]; 

	#if one type makes up a small portion, switch to that type
	permissiableFraction = 1/6; 
	for ant1 in allAnts:
		suma = sum(ant1.counts.values()); 
		for antType in ant1.counts.keys():
			if(ant1.counts[antType]/suma < permissiableFraction):
				#change
				a = 1;
				###################################################################################

if __name__ == '__main__':
	
	pygame.init()

	size = width, height = 900, 700
	white = 255, 255, 255
	fps = 30; 

	screen = pygame.display.set_mode(size)

	primeAnt = pygame.image.load("ant.png"); 
	allAnts = fillAntArray(primeAnt,50); 

	print("Ants loaded");
	clock = pygame.time.Clock();

	#screen.fill(white)
	while 1: 
		for event in pygame.event.get():
		    if event.type == pygame.QUIT: sys.exit()

		for ant in allAnts:
			ant.update(width,height)

		checkCollisions(allAnts); 

		screen.fill(white)
		for ant in allAnts:
			screen.blit(ant.img, ant.rect)
			

		
		clock.tick(fps);
		pygame.display.flip()





