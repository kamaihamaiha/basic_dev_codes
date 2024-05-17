# 条件判断: match case

# 例如，某个学生的成绩只能是A、B、C，用if语句编写如下：
score = 'B'
match score:
    case 'A':
        print('score is A')
    case 'B':
        print('score is B')
    case 'C':
        print('score is C')
    case 'D':
        print('score is D')
    case _: # 表示匹配到其他任何情况
        print('score is valid')

# 复杂匹配
age = 15
match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')        
    case 10:
        print("10 years old.")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old.')
    case _:
        print('not sure.')      

# 匹配列表
# args = ['gcc', 'hello.c', 'world.c']
# args = ['gcc']
args = ['clean']

match args:
    case ['gcc']:
        print('gcc: missing source file(s).')
    case ['gcc', file_1, *files]:
        print('gcc compile: ' + file_1 + ", ".join(files))         
    case ['clean']:
        print('clean...')
    case _:
        print('invalide command.') 

