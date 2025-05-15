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
//
/**
 * 转换规范：%[-+0#](12)(.4)(l)(d)
 * %: 要以这个符号开始
 * [-+0#]: 0个或者多个标志字符
 * 12: 表示字段宽度（可选）
 * .4: 表示保留小数点后4位（可选）
 * l: 长度指示符号（可选）,可用: h\hh\l\ll\z 表示
 * d: 转换操作k（单个字符表示的）
 */
// ：%d, %ld, %lld, %u, %lu, %llu, %c, %f, %e, %E, %o, %x, %X, %s

/**
 * 转换操作
 * c: 字符类型
 * d: 整型
 * e: 双精度浮点型，e计数表示法
 * E: 双精度浮点型，e计数表示法
 * f: 双精度浮点型
 * o: 无符号8进制整型
 * s: 字符型
 * u: 无符号整型
 * x/X: 无符号16进制整型
 */

/**
 * 长度指示符：l, ll, h, hh
 * l: long
 * ll: long long
 * h: short
 * hh: char
 */
//
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

    unsigned int un_ = 0x12345678;
    printf("%x\n", un_);
    printf("%hx\n", un_); // 5678
    printf("%hhx\n", un_); // 78

    // 转换操作：%s
    printf("%s\n", "Hello World\n"); // 获取 sizeof(char *) 字节二进制数据（字符串首地址）

    // 精度控制
    int un = 123;
    double df = 123.456789;

    printf("% .6d\n", un);  // 输出格式最少 6位数字，不够的话补零
    printf("%.0f\n", df);   // 小数点后没有小数
    printf("%.3f\n", df);   // 小数点后保留 3 位

    // 标志：-+0#
    // 0: 使用 0 而不是字符作为 填充字符。如 printf("%03d\n", 12), 打印结果为 012
    // -: 打印时左对齐。如 printf("%-6d\n", 123)
    // +: 打印时，结果显示出符号（正号 + 或者 负号 -）
    // #: 打印时，八进制前面加上 0 或者 十六机制前面加上 X
    printf("%6d\n", 12); // 输出宽度6个字符；不够的前面补充上空格
    printf("%06d\n", 12);
    printf("%-6d end...\n", 12); // 输出宽度6个字符; 左对齐，剩余不够补充的空格在数字后面
    printf("%-+6d\n", 12); // 输出宽度6个字符; 左对齐，结果显示出符号
    printf("%-#6o\n", 12);
    printf("%-#6X\n", 12);

}



