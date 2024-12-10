# if 语句
cars = ['audio', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
	    print(car.title())	
		
# 条件测试
car = 'audi'
print(car.lower() == 'Audi'.lower())

# 检查多个条件

age = 12
print('teen: ', age >= 10 and age < 18)
age = 70
print('do not need work: ', age < 18 or age > 60)

# 检查特定值是否包含在列表中
developed_coutries = ['Britsh', 'Franch', 'Japan', 'America']
print('China' in developed_coutries)
print('Japan' in developed_coutries)
print('China' not in developed_coutries)
