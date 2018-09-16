#maingame.py
import pygame
import windows.window
import events.event
import infos.info

import sys
sys.path.insert(0,'tests/')
import test_draw

#from ..tests import test_draw 

class MainGame(object):
	def __init__(self):
		pygame.init()
		__computer_info = infos.info.Info()
		__window_obj = windows.window.Window((__computer_info.res_info.res_width,__computer_info.res_info.res_height),pygame.FULLSCREEN)
		__event_obj  = events.event.Event()
		
		test_draw.test_blue_rect(__window_obj.get_screen())
		while 1:
			__event_obj.run_logic()
