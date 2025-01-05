import pygame

class Ship():
	"""管理飞船行为"""

	def __init__(self, screen):
		"""初始化飞船，并设置器初始位置"""
		self.screen = screen

		# 加载飞船图形，并获取其外接矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# 把飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_right = False
		self.moving_left = False


	def blitme(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right:
			self.rect.centerx += 1	
		elif self.moving_left:				
			self.rect.centerx -= 1	



