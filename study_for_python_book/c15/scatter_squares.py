import matplotlib.pyplot as plt


def draw_scatter_char_single_point(plt):
    plt.scatter(2, 4, s=200)
    plt.title('scatter chart')
    plt.xlabel('x value...', fontsize=16)
    plt.ylabel('y value...', fontsize=18)
    plt.tick_params(axis='both', labelsize=15)
    plt.show()


def draw_scatter_char_multi_point(plt):
    x_values=[1, 2, 3, 4, 5]
    y_values= [1, 4, 9 , 16, 25]
    # edgecolor 可以指定点的轮廓颜色
    # c 可以指定点的颜色; 也可以用 rgb 表示: c=(0.5,0.5,0,5)
    plt.scatter(x_values, y_values,c=(0.5, 0.5, 0.5),edgecolor='red', s=50)
    plt.title('scatter chart')
    plt.xlabel('x value...', fontsize=16)
    plt.ylabel('y value...', fontsize=18)
    plt.tick_params(axis='both', labelsize=15)
    plt.show()

# 自动绘制批量的点
"""
自定绘制批量的点
use_cmap: 是否用颜色映射
"""
def draw_scatter_char_multi_point_auto(plt, use_cmap):
    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]
    if use_cmap:
        plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=8)
    else:
        plt.scatter(x_values, y_values, s=6)
    plt.title('scatter chart')
    plt.xlabel('x value...', fontsize=16)
    plt.ylabel('y value...', fontsize=18)
    plt.tick_params(axis='both', labelsize=15)

    # 设置坐标轴的取值范围
    plt.axis([0,1100,0,1100000])
    plt.show()


# draw_scatter_char_single_point(plt) 
# draw_scatter_char_multi_point(plt)  
draw_scatter_char_multi_point_auto(plt, True) 