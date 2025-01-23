import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
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

	# 创建一个外星人
	# alien = Alien(ailen_settings, screen)
	aliens = Group()
	gf.create_fleet(ailen_settings, screen, aliens, ship)


	# 开始游戏的主循环
	while True:
		# 监视键盘和鼠标事件
		gf.check_events(ailen_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)	

		# 更新屏幕
		gf.update_screen(screen, ailen_settings, ship, bullets, aliens)


run_game()						
