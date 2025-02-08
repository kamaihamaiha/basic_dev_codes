import matplotlib.pyplot as plt
from random_walk import RandomWalk


def start_walk():
    rw = RandomWalk()
    rw.fill_point()
    # 随机数，用来映射随机颜色
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=8)

    # 单独绘制起点和终点
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=22)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=22)
    
    # 隐藏坐标轴
    cur_axes = plt.gca()
    cur_axes.get_xaxis().set_visible(False)
    cur_axes.get_yaxis().set_visible(False)
    plt.show()

# start_walk() 

# 不断walk，直到主动退出; 注意，要在终端中运行
while True:
    start_walk()
    keep_running = input("make another wald?(y/n):")
    if keep_running == 'n':
        break

