import sys

import pygame
from bullet import Bullet
from alien import Alien

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
	if event.key == pygame.K_q:
		sys.exit()
	if event.key == pygame.K_RIGHT:
		# 只修改飞船的moving_right标记
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		ship.moving_left = True	
	if event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)
					
def check_key_up_event(event, ship):
	if event.key == pygame.K_RIGHT:
		# 只修改飞船的moving_right标记
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False		

def update_screen(screen, settings, ship, bullets, aliens):
	# 绘制背景
	screen.fill(settings.bg_color)

	# 绘制子弹
	for bullet in bullets:
		bullet.draw_bullet()	

	# 绘制飞船
	ship.blitme()	

	# 绘制外星人
	for alien in aliens:
		alien.blitme()		

	# 让最近绘制的屏幕可见
	pygame.display.flip()	


def update_bullets(bullets):
	bullets.update()
	# 删除已经消失的子弹; 使用 copy() 可以在循环中修改
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	print(len(bullets))		


def fire_bullet(settings, screen, ship, bullets):
	# 限制子弹数量		
	if len(bullets) < settings.bullet_allowed:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)	


def create_fleet(settings, screen, aliens):
	# 创建一群外星人
	alien = Alien(settings, screen)
	available_width = settings.screen_size[0] - settings.alien_margin * 2
	alien_count = int(available_width / (alien.rect.width + settings.alien_margin))
	for alien_index in range(alien_count):
		alien = Alien(settings, screen)
		alien.x = settings.alien_margin + alien_index * (alien.rect.width + settings.alien_interval)
		alien.rect.x = alien.x
		aliens.add(alien)




