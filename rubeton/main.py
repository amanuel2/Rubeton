#maingame.py
import pygame
import windows.window
import events.event

class MainGame(object):
	def __init__(self):
		pygame.init()
		__window_obj = windows.window.Window((500,500), pygame.RESIZABLE)
		__event_obj  = events.event.Event(__window_obj)
		while 1:
			__event_obj.run_logic()

if __name__ == '__main__':
	mg = MainGame()
