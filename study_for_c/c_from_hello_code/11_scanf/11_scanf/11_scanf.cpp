// 11_scanf.cpp : 
// VS 2019 之后默认不让用 scanf，会提示如下错误：
// 严重性	代码	说明	项目	文件	行	禁止显示状态
// 错误	C4996	'scanf': This function or variable may be unsafe.Consider using scanf_s instead.To disable deprecation, use _CRT_SECURE_NO_WARNINGS.See online help for details.	11_scanf	D : \codes\Cpp\11_scanf\11_scanf\11_scanf.cpp	9


#include <iostream>
/**
 * 注意:
 * 如果 scanf 要存入基本变量，则在变量名前加 &
 * 如果 scanf 要存入字符数组中，则字符数组名不用加 &
 * @return
 */
int main() {
    char c;
    short s;
    int n;
    long l;
    float f;
    double df;

    // 输入基本数据类型
    printf("Please input nums: char, short, int, long, float, double");
    scanf("%hhd %hd %d %ld %f %lf", &c, &s, &n, &l, &f, &df); // 注意第一个参数里面的格式都是数字之间加空格，因此输入数字时，也要用空格隔开
    printf("%d %d %d %ld %2.1f %2.2f\n", c, s, n, l, f, df);

    // 输入字符
    char c_;
    scanf("%hhd", &c_); // 必须输入字符对应的 ASCII值; 因为是当作 整型char输入的
    printf("%d, %c\n", c_, c_);

    // 清除输入缓冲区中的任何残留字符
    while (getchar() != '\n');

    char cc;
    printf("please input char:\n");
    scanf(" %c\n", &cc);
    printf("%d, %c\n", cc, cc);

    // 输入字符串：C语言没有字符串类型，要用字符数组表示
    printf("please input char...");
    char str[10];
    scanf("%s", &str[0]);
    printf("%s\n", str);
    return 0;
}


