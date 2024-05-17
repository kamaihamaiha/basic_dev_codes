# 循环: for & while

# for

names = ['Michale', 'Bob', 'Tracy']
for name in names:
    print(name)

for value in [1, 2, 3, 4]:
    print(value)  


# range() 可以生成整数序列, list() 可以把整数序列转换成list
vars = list(range(3))
for var in vars:
    print(var)


# 计算 1-100 的和; range 从0开始，所以计算到100，要写成 101
sum = 0;
for x in range(101):
    sum += x
print('sum: %d' % sum)    


# while
sum = 0
n = 1
while n <= 100:
    sum += n
    n = n + 1
print('sum: %d' % sum)    


# 练习，对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print('hello, %s!' % l)