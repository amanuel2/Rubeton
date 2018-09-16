#events.py
import pygame
import sys
import kbd.Keyboard


class Event(object):
		def __init__(self):
			self.Keyboard = kbd.Keyboard.Keyboard()
			
		def run_logic(self):
			for event in pygame.event.get():
				self.Keyboard.run_key_events(event)
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip() 
