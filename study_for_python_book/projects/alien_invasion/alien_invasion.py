import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

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
		gf.check_events()

		# 更新屏幕
		gf.update_screen(screen, ailen_settings, ship)


run_game()						
