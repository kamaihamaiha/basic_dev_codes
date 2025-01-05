import sys

import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
	# 监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				check_key_down_event(settings, screen, event, ship, bullets)
					
			elif event.type == pygame.KEYUP:
				check_key_up_event(event, ship)

def check_key_down_event(settings, screen, event, ship, bullets):
	if event.key == pygame.K_RIGHT:
		# 只修改飞船的moving_right标记
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True	
	if event.key == pygame.K_SPACE:
		# 限制子弹数量
		if len(bullets) < settings.bullet_allowed:
			new_bullet = Bullet(settings, screen, ship)
			bullets.add(new_bullet)	
					
def check_key_up_event(event, ship):
	if event.key == pygame.K_RIGHT:
		# 只修改飞船的moving_right标记
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False		

def update_screen(screen, settings, ship, bullets):
	# 绘制背景
	screen.fill(settings.bg_color)

	# 绘制子弹
	for bullet in bullets:
		bullet.draw_bullet()	

	# 绘制飞船
	ship.blitme()			

	# 让最近绘制的屏幕可见
	pygame.display.flip()				