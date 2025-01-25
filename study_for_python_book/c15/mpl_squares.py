import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values,squares, linewidth=5)
plt.title("this is a demo squares", fontsize=24)
plt.xlabel("x value...", fontsize=24)
plt.ylabel("y value...", fontsize=16)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
