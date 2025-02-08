import matplotlib.pyplot as plt
from random_walk import RandomWalk


def start_walk():
    rw = RandomWalk()
    rw.fill_point()
    plt.scatter(rw.x_values, rw.y_values, s=8)
    plt.show()

# start_walk() 

# 不断walk，直到主动退出; 注意，要在终端中运行
while True:
    start_walk()
    keep_running = input("make another wald?(y/n):")
    if keep_running == 'n':
        break

