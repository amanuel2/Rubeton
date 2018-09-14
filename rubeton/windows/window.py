#window.py
import pygame

class Window(object):
	def __init__(self,size,_FLAG_1=0,_FLAG_2=0):
		self.__window = pygame.display.set_mode(size,_FLAG_1,_FLAG_2)
		
		
