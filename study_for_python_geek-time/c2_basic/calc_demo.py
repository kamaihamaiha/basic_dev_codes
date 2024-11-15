# 简单的计算器
num1 = input("please input num1:")
num2 = input("please input num2:")

opera = input("请输入运算符:")
# print("计算结果: ", eval(f"{num1}{opera}{num2}"))
ret = eval(f"{num1}{opera}{num2}")
print(f"计算结果: {ret}")