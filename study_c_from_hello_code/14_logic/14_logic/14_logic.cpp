﻿// 14_logic.cpp : 
// 关系运算符的表达式值：0 为 假，1 为真
#include <stdio.h>

// 操作符优先级：从高到低
// ++ -- 后缀
// ++ -- 前缀
// !
// + - 正号、负号
// * / %
// + -
// < > <= >= == !=
// && ||
// =

int main()
{
   
	printf("%d\n", 0 == 0); // 输出 1
	printf("%d\n", 0 > 0);  // 输出 0

	return 0;
}

