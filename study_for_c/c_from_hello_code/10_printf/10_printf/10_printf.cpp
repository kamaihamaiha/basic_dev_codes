// 10_printf.cpp : 
//

#include <iostream>

int main()
{
    unsigned long l = 4294967295; // 该类型能表示的最大数字
    unsigned long long ll = 18446744073709551615;
    
    // %u 或 %d 仅获取 4个字节数据
    printf("%u\n", l);
    printf("%u %u\n", ll); // 会输出 4294967295 4294967295 

    // lld llu 增加转换数据字节长度
    printf("%llu\n", ll);

    return 0;
}


