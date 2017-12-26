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
import matplotlib.pyplot as plt


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



def checkCollisions(allAnts,primeAnt):

	#update counts
	for ant1 in allAnts:
		for ant2 in allAnts:
			if(ant2.ID not in ant1.encounters and ant1.rect.colliderect(ant2.rect)):
				ant1.encounters.append(ant2.ID); 
				ant1.counts[ant2.__class__.__name__] += 1; 

	#drop oldest encounters
	# totalEncounters = 50; 
	# for ant1 in allAnts:
	# 	if(len(ant1.encounters) > totalEncounters): 
	# 		ant1.encounters = ant1.encounters[-totalEncounters:-1];
			

	#if one type makes up a small portion, switch to that type
	permissiableFraction = .19; 
	for ant1 in allAnts:
		suma = sum(ant1.counts.values()); 
		for antType in ant1.counts.keys():
			if(ant1.counts[antType]/suma < permissiableFraction and antType is not "AntSprite"):
				#change
				#print("{} to {}".format(ant1.__class__.__name__,antType));
				newAntType = eval(antType); 
				newAnt = newAntType(primeAnt); 
				newAnt.rect.move(ant1.rect[0],ant1.rect[1]); 
				newAnt.setNewGoal(); 
				allAnts.append(newAnt);
				allAnts.remove(ant1); 
				break;  
	
def theCulling(allAnts,primeAnt):
	toRem = []; 
	perToRem = .0001; 
	for i in range(0,len(allAnts)):
		if(np.random.random()<perToRem):
			toRem.append(allAnts[i]); 

	for i in range(0,len(toRem)):
		allAnts.remove(toRem[i]); 
		allAnts.append(AntSprite(primeAnt)); 

def roleCall(allAnts,allCounts):
	counts = {"BuilderAnt":0,"SoliderAnt":0,"GathererAnt":0,"NurseAnt":0,"AntSprite":0};
	for ant in allAnts:
		counts[ant.__class__.__name__] += 1; 

	for count in counts.keys():
		allCounts[count].append(counts[count]); 
	

if __name__ == '__main__':
	
	pygame.init()

	size = width, height = 900, 700
	white = 255, 255, 255
	fps = 30; 
	numAnts = 75; 

	allCounts = {"BuilderAnt":[],"SoliderAnt":[],"GathererAnt":[],"NurseAnt":[],"AntSprite":[]};

	screen = pygame.display.set_mode(size)

	primeAnt = pygame.image.load("ant.png"); 
	allAnts = fillAntArray(primeAnt,numAnts); 

	print("Ants loaded");
	clock = pygame.time.Clock();

	myfont = pygame.font.SysFont("monospace",15); 

	#screen.fill(white)
	quitFlag=False; 
	while 1: 
		for event in pygame.event.get():
		    if(event.type == pygame.QUIT):
		    	pygame.display.quit();
		    	quitFlag = True; 
		if(quitFlag):
			break;  

		for ant in allAnts:
			ant.update(width,height)
 
 		roleCall(allAnts,allCounts); 
 		#set labels
 		labels = []; 
 		for key in allCounts.keys():
 			labels.append(myfont.render(key+": "+str(allCounts[key][-1]),1,(0,0,0))); 



		checkCollisions(allAnts,primeAnt); 
		theCulling(allAnts,primeAnt); 
		screen.fill(white)
		for ant in allAnts:
			screen.blit(ant.img, ant.rect)
		for i in range(0,len(labels)):
 			screen.blit(labels[i],(50+i*175,50)); 

		
		clock.tick(fps);
		pygame.display.flip()

	leg = []; 
	for key in allCounts.keys():
		plt.plot(allCounts[key]); 
		leg.append(key); 
	plt.legend(leg); 
	plt.show();

