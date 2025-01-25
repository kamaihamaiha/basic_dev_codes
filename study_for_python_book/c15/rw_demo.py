import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_point()
plt.scatter(rw.x_values, rw.y_values, s=8)
plt.show()