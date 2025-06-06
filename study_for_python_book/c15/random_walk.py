from random import choice

class RandomWalk():
    """随机漫步，记录漫步次数和轨迹"""
    def __init__(self, num_points=50000):
        self.num_points = num_points
        # 初始点都为0
        self.x_values=[0]
        self.y_values=[0]

    def fill_point(self):
        # 不断漫步，直到跑完所有的点
        while(len(self.x_values) < self.num_points):
            # 方向和距离决定 step
            x_direction = choice([-1,1])
            x_distance = choice([0, 1, 2, 3, 4])   
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4])   
            y_step = y_direction * y_distance

            # 下一步的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


