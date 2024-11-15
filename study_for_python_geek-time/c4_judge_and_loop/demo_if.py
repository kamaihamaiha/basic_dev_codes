import random

conn = 10 < 9
if conn:
    print('this is Ture.')
else:
    print('this is False')    

age_str = input('please input your age:')
age = int(age_str)
if age <= 1:
    print('infant')
elif age <=6:
    print('baby')   
elif age <= 10:
    print('toddler')
elif age <= 18:
    print('tennager')
elif age <= 30:
    print('yong man/woman')
elif age < 60:
    print('middle-agged')
else:
    print('elderly')    

# 课后习题
# 变量 number 是随机生成的 1~100 的整数，请使用 if 语句判断每次产生的随机数，是否能被 3 整除，并将执行结果输出到命令行。

num = int(random.random() * 100 + 1)

if num % 3 == 0:
    print(f"{num} 可以被3整除")
else:
    print(f"{num} 不能被3整除")    