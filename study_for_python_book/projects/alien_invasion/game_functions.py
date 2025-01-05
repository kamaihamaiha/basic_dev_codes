import sys

import pygame

def check_events():
	# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


def update_screen(screen, settings, ship):
	# 绘制背景
	screen.fill(settings.bg_color)	

	# 绘制飞船
	ship.blitme()			

	# 让最近绘制的屏幕可见
	pygame.display.flip()				