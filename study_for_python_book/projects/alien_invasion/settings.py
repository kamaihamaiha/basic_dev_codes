class Settings():
	"""存储 《外星人入侵》的所有设置的类"""
	def __init__(self):
		self.screen_size = (1200, 800)
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5
		self.window_caption = 'Alien Invasion'

		# 子弹参数设置
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullet_allowed = 3

		# 外星人左右距离屏幕边缘的距离
		self.alien_margin = 30
		# 外星人之间距离
		self.alien_interval = 50
		self.alien_margin_top = 30