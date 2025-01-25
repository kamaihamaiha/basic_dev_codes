import matplotlib.pyplot as plt


def draw_cub(plt, num=5):
    x_values = list(range(1, num+1))
    y_values = [x**3 for x in x_values]

    plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=8)
    plt.title('simple cube')
    plt.xlabel('x value...', fontsize=15)
    plt.ylabel('y value...', fontsize=15)

    plt.tick_params(axis='both', labelsize=15)
    plt.show()

draw_cub(plt, 5000)    