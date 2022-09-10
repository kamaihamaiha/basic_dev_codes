// 21_string_char-array.cpp :
// 字符串与字符数组
// 1. 字符数组 2种初始化方式
// 2. 打印字符数组，也有 2种方式
// 3. 测量字符数组里字符的个数：for 循环或者 strlen() 函数
// 4. 从键盘输入字符串到字符数组
// 5. 输入输出字符串除了 scanf 和 printf 外 getchar putchar 能输入或输出单个字符

#include <stdio.h>
#include <string.h>

int main()
{
	// 字符数组 2种初始化方式: 初始化列表和字面值常量。 注意 = 左边的 [] 内的数字 10 也可以不写
	char str1[10] = { 'H', 'e', 'l', 'l', 'o'};

	char str2[6] = "Hello";

	// 打印字符数组，也有 2种方式
	printf(str1);

	printf("\n");

	printf("%s\n", str2);

	// 测量字符数组里字符的个数：for 循环或者 strlen() 函数

	int c_count = 0;
	for (int i = 0; i < sizeof(str1); i++) {
		if (str1[i] != '\0') {
			c_count++;
		}
	}
	printf("数组 str1 的字符个数：%d\n", c_count);

	printf("数组 str1 的字符个数: %d\n", strlen(str1));

	// 4.从键盘输入字符串到字符数组
	char str3[20];
	//scanf("%s", str3);

	//printf(str3);

	// 5. getchar & putchar
	printf("请输入字符：\n");
	char c;
	c = getchar();
	c = c - 32; // 转换成大写字母
	putchar(c);
	
	return 0;
}

