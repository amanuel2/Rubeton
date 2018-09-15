#kbd.py
import pygame
import keys.esc

class Keyboard(object):
	
	def __init__(self):
		pass

	def run_key_events(self,event):
		self.key_conditions(event)
		
	def key_conditions(self,event):
		if event.type == pygame.KEYUP:
			self.key_up(event)
		elif event.type == pygame.KEYDOWN:
			self.key_down(event)
		else:
			pass
		
			
	def key_up(self,event):
		pass
		
		
	def key_down(self,event):
		if event.key == pygame.K_ESCAPE:
			keys.esc.esc_key()
		else:
			pass
		
		

