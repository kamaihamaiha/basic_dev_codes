import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	def __init__(self, settings, screen, ship):
		super().__init__()

		self.screen = screen
		# 在(0,0)处，创建一个表示子弹的矩形，再设置正确的位置
		self.rect = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y) 
		self.color = settings.bullet_color
		self.speed_factor = settings.bullet_speed_factor


	def update(self):
		"""移动子弹"""
		self.y -= self.speed_factor
		self.rect.y = self.y

	def draw_bullet(self):
		"""在屏幕上绘制子弹"""
		pygame.draw.rect(self.screen, self.color, self.rect)			