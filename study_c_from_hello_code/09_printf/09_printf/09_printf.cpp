// 09_printf.cpp : 
// printf 是一个变参函数
// printf first parma must be string
// char, short, int => %d
// long => %ld
// long long => %lld
// 无符号整型占位符：%u
// unsigned char, unsigned short, unsigned int => %u
// unsigned long => %lu
// unsigned long long => %llu
// 转换规范：%[-+0#](12)(.4)(l)(d)
// 转换操作：%d, %ld, %lld, %u, %lu, %llu, %c, %f, %e, %E, %o, %x, %X, %s

// 长度指示符：l, ll, h, hh
// 比如（加长）：%d => sizeof(int), %lld => sizeof(long long), %x => sizeof(unsigned int), %llx => sizeof(unsigned long long)
// 比如(缩短)：%x => sizeof(unsigned int), %hx => sizeof(unsigned short), %hhx => sizeof(unsigned char)

// 精度: 
// 如：.4 => 点号表示精度范围，后面跟着十进制正数
// 如果是整型：精度可以控制最少多少位数字
// 如果是浮点型：精度可以控制小数点后的位数
// 

// 最小宽度
// %3d, %8f

// 标志：-+0#
// 0: 使用 0 而不是字符作为 填充字符。如 printf("%03d\n", 12), 打印结果为 012
// -: 打印时左对齐。如 printf("%-6d\n", 123)
// +: 打印时，结果显示出符号（正号 + 或者 负号 -）
// #: 打印时，八进制前面加上 0 或者 十六机制前面加上 X


#include <iostream>

int main()
{
    int a = 1;
    float b = 2.1;
    char c = 'a';

    printf("整型a为%d, 浮点b为%f, 字符c为%c\n", a, b, c);

    // float 进入 printf 会转换成 double 类型输出
    float fv = 1.234;
    double dv = 1.234567;
    printf("%f\n", fv);
    printf("%f\n", dv);
    // 使用科学计数法：%e、%E
    printf("%e\n", fv);
    printf("%E\n", fv);

    // 转换操作：%u %o %x %X
    unsigned int n = 123456;
    printf("%u\n", n);
    printf("%o\n", n); // 八进制
    printf("%x\n", n); // 十六进制
    printf("%X\n", n); // 十六进制

    // 转换操作：%s
    printf("%s\n", "Hello World\n"); // 获取 sizeof(char *) 字节二进制数据（字符串首地址）

    // 精度控制
    int un = 123;
    double df = 123.456789;

    printf("% .6d\n", un);  // 输出格式最少 6位数字，不够的话补零
    printf("%.0f\n", df);   // 小数点后没有小数
    printf("%.3f\n", df);   // 小数点后保留 3 位

    // 
}



