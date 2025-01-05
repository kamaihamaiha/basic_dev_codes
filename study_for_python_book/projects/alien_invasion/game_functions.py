import sys

import pygame

def check_events(ship):
	# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					# 只修改飞船的moving_right标记
					ship.moving_right = True
				if event.key == pygame.K_LEFT:
					ship.moving_left = True	
					
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					# 只修改飞船的moving_right标记
					ship.moving_right = False
				if event.key == pygame.K_LEFT:
					ship.moving_left = False	



def update_screen(screen, settings, ship):
	# 绘制背景
	screen.fill(settings.bg_color)	

	# 绘制飞船
	ship.blitme()			

	# 让最近绘制的屏幕可见
	pygame.display.flip()				