// 11_scanf.cpp : 
// VS 2019 之后默认不让用 scanf，会提示如下错误：
// 严重性	代码	说明	项目	文件	行	禁止显示状态
// 错误	C4996	'scanf': This function or variable may be unsafe.Consider using scanf_s instead.To disable deprecation, use _CRT_SECURE_NO_WARNINGS.See online help for details.	11_scanf	D : \codes\Cpp\11_scanf\11_scanf\11_scanf.cpp	9


#include <iostream>

int main()
{
    char c;
    short s;
    int n;
    long l;
    float f;
    double df;

   // scanf("%hhd %hd %d %ld %f %lf", &c, &s, &n, &l, &f, &df);
   // printf("%d %d %d %d %2.1f %2.2f\n", c, s, n, l, f, df);
   // scanf("%hhd", &c);
   // printf("%c\n", c);

    // 输入字符串：C语言没有字符串类型，要用字符数组表示
    char str[10];
    scanf("%s", &str[0]);
    printf("%s\n", str);
    return 0;
}


