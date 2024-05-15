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
