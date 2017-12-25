import pygame
import numpy as np
import string
import random 

class AntSprite:

	def __init__(self,surf):
		
		self.img = surf.copy();
		self.img = pygame.transform.scale(self.img,(10,10));
		self.rect= self.img.get_bounding_rect()
		self.rect = self.rect.move([np.random.randint(100,800),np.random.randint(100,600)]);

		self.allGoals = [];
		for i in range(0,30):
			self.allGoals.append([np.random.randint(100,800),np.random.randint(100,600)]); 
		self.setNewGoal(); 

		self.makeID(); 
		self.counts = {"BuilderAnt":100,"SoliderAnt":100,"GathererAnt":100,"NurseAnt":100,"AntSprite":100};

		#keep list of encountered ants
		self.encounters = [];

	def goalDist(self):
		return np.sqrt((self.rect.center[0]-self.goal[0])**2 + (self.rect.center[1]-self.goal[1])**2)

	def makeID(self): 
		s=string.lowercase+string.digits
		self.ID = ''.join(random.sample(s,20))

	def reColor(self):
		arr = pygame.surfarray.pixels3d(self.img); 
		#print(arr); 
		arr[:,:,0] = self.color[0]; 
		arr[:,:,1] = self.color[1]; 
		arr[:,:,2] = self.color[2]; 

	def setNewGoal(self):
		self.goal = self.allGoals[np.random.randint(0,len(self.allGoals))]; 

		self.speed = [self.goal[0]-self.rect.center[0],self.goal[1]-self.rect.center[1]]; 
		suma = abs(self.speed[0])+abs(self.speed[1]); 
		self.speed[0] = self.speed[0]*10/suma; 
		self.speed[1] = self.speed[1]*10/suma; 

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

		#have counts fade with time to prioritize recent weightings
		for antType in self.counts.keys():
			self.counts[antType] -= 0.0001; 

		#make sure counts don't go below zero
		for antType in self.counts.keys():
			self.counts[antType] = max(self.counts[antType],0); 



class BuilderAnt(AntSprite):

	def __init__(self,surf):
		AntSprite.__init__(self,surf); 
		self.allGoals = [[100,100],[500,500],[800,100]];
		self.color = [0,0,200];
		self.img.convert_alpha(); 
		self.reColor();  
		self.setNewGoal(); 

class SoliderAnt(AntSprite):
	def __init__(self,surf):
		AntSprite.__init__(self,surf); 
		self.allGoals = [[100,500],[500,100],[800,500]];
		self.color = [200,0,0];
		self.img.convert_alpha(); 
		self.reColor();  
		self.setNewGoal();

class GathererAnt(AntSprite):
	def __init__(self,surf):
		AntSprite.__init__(self,surf);  
		self.allGoals = [[100,100],[500,500],[500,100],[100,500]];
		self.color = [0,200,0];
		self.img.convert_alpha(); 
		self.reColor();  
		self.setNewGoal();

class NurseAnt(AntSprite):
	def __init__(self,surf):
		AntSprite.__init__(self,surf);  
		self.allGoals = [[300,300],[600,600],[600,300],[300,600]];
		self.color = [150,0,150];
		self.img.convert_alpha(); 
		self.reColor();  
		self.setNewGoal();

