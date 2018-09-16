#resolution.py
import pygame

class Resolution(object):
	def __init__(self):
		self.res_width  = 0
		self.res_height = 0
		self.get_width()
		self.get_height()
	
	def get_width(self):
		self.res_width = pygame.display.Info().current_w
	
	def get_height(self):
		self.res_height = pygame.display.Info().current_h
