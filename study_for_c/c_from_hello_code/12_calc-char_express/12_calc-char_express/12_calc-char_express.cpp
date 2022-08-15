// 12_calc-char_express.cpp : 运算符和表达式
// 
// ++ -- : 分成两个作用：对表达式作用、对运算对象的额外作用
// 额外作用在不同编译器有不同的发生时机：VS 积累所有子表达式求值后才会进行额外作用；gcc 每完成一个子表达式就会立刻产生额外作用
//

#include <iostream>

int main()
{
    // 前缀模式
    int a = 10;
    int b = 10;
    printf("%d, %d\n", ++a, --b);
    printf("%d, %d\n", a, b);

    // 后缀模式
    int c = 10;
    int d = 10;
    printf("%d, %d\n", c++, d--); // 表达式结果不会改变，但是会额外改变 变量 c 和 d 的值
    printf("%d, %d\n", c, d);

    int j, k;
    j = 1;
    k = j++ + j++ + j++;
    printf("%d %d\n", j, k); // 结果是：4 3 （VS编译器）
    return 0;
 }

