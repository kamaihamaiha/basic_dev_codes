# 递归函数

# 计算 斐波那契数列
def fibonacci(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2);

num_str = input('please type a num:')
print("ret: %d" % fibonacci(int(num_str)))

# 练习 汉诺塔: 参数n表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法
def hanoiTower(n , a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoiTower(n - 1, a, c, b) # 因为超过1个，则先从 a move 到 b       
        print(a, '-->', c)
        hanoiTower(n - 1, b, a, c) # 再从 b move 到 c


num_str = input('please type a num:')
hanoiTower(int(num_str), 'A', 'B', 'C')