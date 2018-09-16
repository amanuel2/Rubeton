#test_draw.py
import pygame

def test_blue_rect(screen):
	BLUE_RGB = (0,128,255)
	rect_test = pygame.Rect(0,0,300,300)
	pygame.draw.rect(screen,BLUE_RGB, rect_test)
