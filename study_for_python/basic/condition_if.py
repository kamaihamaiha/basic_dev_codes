# 条件判断: if else

age = 20

if age <= 18:
    print("child")
else:
    print('adult')   

if age < 6:
    print('baby')     
elif age < 18:
    print('student')   
elif age > 60:
    print('old man')
else:
    print('worker')   

# 直接用变量或者字面值也可以
if age:
    print('age > 0')    

if 'x':
    print('string is not null')

if [1, 2]:
    print('list is not empty')    


# input 使用
str = input('Please type your age: ')
age = int(str)

if age < 18:
    print('you are teenager')
elif age >= 60:
    print('you are a old!')    
else:
    print('middle aged')    


print('计算BMI指数:')

# 练习: 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖  

str_h = input('type your height(unit/cm): ')
str_w = input('type your weight(unit/kg): ')
height = int(str_h) / 100
weight = int(str_w)
bmi = weight / (height * height)  

print(f'bmi: {bmi:.2f}')
if bmi < 18.5:
    print('5：过轻') 
elif bmi < 25:    
    print('正常') 
elif bmi < 28:    
    print('过重') 
elif bmi < 32:    
    print('肥胖') 
else: 
    print('严重肥胖') 