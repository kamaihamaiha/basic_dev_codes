import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""管理外星人的类"""

	def __init__(self, ai_settings, screen):
		super().__init__()
		self.ai_settings = ai_settings
		self.screen = screen

		# 加载外星人图形
		self.img = pygame.image.load('images/alien.bmp')
		self.rect = self.img.get_rect()
		self.screen_rect = self.screen.get_rect()

		# 每个外星人最初在屏幕左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# 存储精确的位置
		self.x = float(self.rect.x)


	def blitme(self):
		self.screen.blit(self.img, self.rect)