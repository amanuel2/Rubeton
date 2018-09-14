#events.py
import pygame
import sys

class Event(object):
		def __init__(self,screen):
			pass
		def run_logic(self):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip() 
