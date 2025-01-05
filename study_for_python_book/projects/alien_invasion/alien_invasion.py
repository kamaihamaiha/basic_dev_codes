import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	"""初始化游戏，并创建一个屏幕对象"""
	pygame.init()
	ailen_settings = Settings()
	screen = pygame.display.set_mode(ailen_settings.screen_size)
	pygame.display.set_caption(ailen_settings.window_caption)

	# 创建一个飞船
	ship = Ship(screen, ailen_settings)

	# 创建一个编组，存储子弹用
	bullets = Group()


	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ailen_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		# 删除已经消失的子弹; 使用 copy() 可以在循环中修改
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)

		print(len(bullets))		

		# 更新屏幕
		gf.update_screen(screen, ailen_settings, ship, bullets)


run_game()						
