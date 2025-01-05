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
		# 绘制背景
		#screen.fill(ailen_settings.bg_color)	

		# 绘制飞船
		#ship.blitme()			

		# 让最近绘制的屏幕可见
		#pygame.display.flip()


run_game()						
