# 实参，分为: 位置实参, 关键字实参, list, dict

# 位置实参
def describe_pet(type, name):
	print("\nI have a " + type + ".")
	print("\nMy " + type + "'s name is " + name.title() + ".")

describe_pet('hamster', 'harry')	
describe_pet('dog', 'willie')	


# 关键字实参
describe_pet(type='dog', name='Lucy')
describe_pet(name='Bom', type='Lion')

# 默认值
def describe_petv2(name, type='cat'):
	print("\nI have a " + type + ".")
	print("\nMy " + type + "'s name is " + name.title() + ".")
describe_petv2('Bush')
describe_petv2('Bush', 'Bird')