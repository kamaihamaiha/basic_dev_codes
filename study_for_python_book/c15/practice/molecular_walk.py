from random import choice

class MolecularWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 设置初始点
        self.x_values=[0]
        self.y_values=[0]

    def fill_point(self):
        # 不断漫步，直到跑完所有的点
        while(len(self.x_values) < self.num_points):
            # 方向和距离决定 step
            x_step = self.get_step()

            y_step = self.get_step()

            # 下一步的位置
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        cur_direction = choice([-1, 1])
        cur_distance = choice([0, 1, 2, 3, 4])
        cur_step = cur_direction * cur_distance
        return cur_step