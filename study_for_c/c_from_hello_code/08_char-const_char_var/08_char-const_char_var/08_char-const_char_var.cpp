// 08_char-const_char_var.cpp : 字符常量和字符变量
// 字符常量：用单引号
// 字符变量：char. 字符类型其实就是整型类型，只不过字符类型只占用一个字节
// 字符串占用空间大小
// \数值(八进制): 转义字符

#include <iostream>

int main()
{
    // 字符常量占用的字节大小，根据编译器而不同。如果是 C编译器那么是 4Byte，如果是 C++编译器则为 1Byte
    printf("sizeof a=%d\n", sizeof('a'));
    printf("sizeof b=%d\n", sizeof('b'));

    // 例题：把大写字母 A 转换成小写字母 a
    char letter = 'A';
    letter += 32;
    printf("%c\n", letter);

    // sizeof string
    printf("sizeof hello = %d\n", sizeof("hello"));

    // 加上个空字符 \0 表示字符串的结尾，那么就只会打印出 hello 
    printf("hello\0World\n");

    printf("\n\n");

    // 使用 \数值(八进制): 转义字符 形式打印
    printf("\110\145\154\154\157\n");
}


