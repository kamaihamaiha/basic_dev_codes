import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
	"""初始化游戏，并创建一个屏幕对象"""
	pygame.init()
	ailen_settings = Settings()
	screen = pygame.display.set_mode(ailen_settings.screen_size)
	pygame.display.set_caption("Alien Invasion")

	# 创建一个飞船
	ship = Ship(screen)


	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		# 绘制背景
		screen.fill(ailen_settings.bg_color)	

		# 绘制飞船
		ship.blitme()			

		# 让最近绘制的屏幕可见
		pygame.display.flip()


run_game()						
