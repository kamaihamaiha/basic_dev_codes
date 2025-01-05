import sys
import pygame

def show_window():
	"""创建一个背景为蓝色的 Pygame 窗口"""
	bg_color = (0, 0, 220)
	size = (1000, 700)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("this is a blue window")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(bg_color)
		pygame.display.flip()


show_window()	