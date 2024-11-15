# match 从 python 3.10 开始支持

code = 400
match code:
    case 100:
        print('code is 100')
    case 200:
        print('code is 200')
    case 300 | 400:
        print('code is 300 or 400')
    case _:
        print('other')

# 练习: 输入月份，输出季节
month = int(input('please input month:'))
match month:
    case 3 | 4 | 5:
        print('spring')        
    case 6 | 7 | 8:
        print('summer')        
    case 9 | 10 | 11:
        print('autumn')        
    case 12 | 1 | 2:
        print('winter')  
    case _:
        print('wrong input!')              
