import sys
import pygame

def show_window():
	"""创建一个背景为蓝色的 Pygame 窗口"""
	bg_color = (0, 0, 220)
	size = (1000, 700)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("this is a blue window")
	# 角色头像
	avatar = pygame.image.load('debug.jpg')
	avatar_rect = avatar.get_rect()
	avatar_rect.centerx = screen.get_rect().centerx
	avatar_rect.centery = screen.get_rect().centery

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(bg_color)
		screen.blit(avatar, avatar_rect)
		pygame.display.flip()


show_window()	