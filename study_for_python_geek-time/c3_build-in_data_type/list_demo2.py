# 列表常见操作: add,modify,length,sort

# insert(), append(), extend(可迭代对象*)

citys = ['Beijing']
print(citys)
citys.insert(0,'Shanghai')
print(citys)
citys.append('HongKong')
print(citys)

citys.extend("ABC")
print(citys)

# remove, reverse, pop(index), copy, clear
citys.reverse()
print(citys)
citys.reverse
citys.remove('C')
print(citys)
print(citys.pop(0))
print(citys)

citys_tmp = citys.copy
print(citys_tmp)
citys_tmp.clear()