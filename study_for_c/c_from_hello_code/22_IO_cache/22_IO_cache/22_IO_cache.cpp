// 22_IO_cache.cpp : 输入输出缓存
// Windows 系统下输出 hello world 10次，然后每次都等待 500ms. 头文件用 windows.h，休眠用 Sleep(ms)
// Linux 系统下输出 hello world 10次，然后每次都等待 500ms. 头文件用 unistd.h，休眠用 usleep(us)

// 输出缓存
/*
 输出字符会暂时缓存在 缓存区，等待时机再批量处理，发送给显卡。
 Windows 系统：立刻刷新缓存区
 Linux 系统：累计数据，直到程序结束

 行缓存：一行结束后，必须刷新缓存。\n 表示一行结束
 完全缓存：等到缓存区被填满，才刷新缓存
*/

// 输入缓存
/*
 输入函数是阻塞函数

 scanf: 输入字符串
 getchar: 输入一个字符
 getch: 无缓存输入函数. 在 conio.h 中
 getche: 无缓存输入函数. 在 conio.h 中. 会自动打印到控制台，连 putchar 都不需要
*/

// 为了区分平台实现函数和C语言标准函数，会在平台实现函数前加 _ , 如：_getch _getche

#include <stdio.h>
#include <windows.h>
#include <conio.h>

void inputChar();
void input();
void input_new();

int main()
{
	// 输出
	for (int i = 0; i < 10; i++) {
		printf("Hello World %d\n", i);
		Sleep(100);
	}

	// 输入
	// inputChar();

	// 使用 getchar 输入字符串
	//input();

	// 使用 getch
	input_new();

	return 0;
}

void inputChar() {
	// 输入
	char c1, c2, c3;
	c1 = getchar();
	putchar(c1);

	// 吸收掉上面的代码执行后，缓存区的内容
	getchar();

	c2 = getchar();
	putchar(c2);

	getchar();
	c3 = getchar();
	putchar(c3);

}

void input() {

	char str[20];
	int i = 0;
	while (i < 20 - 1) {
		char c;
		c = getchar();
		str[i++] = c; 

		// 输入回车后结束
		if (c == '\n') {
			break;
		}
	}

	// 字符串结尾要加上 0，标记结束 
	str[i] = '\0';
	printf(str);

	// 如果输入的字符数超过了 19 个，剩下的则会继续留在 输入缓存区。因此可以把剩下的内容打印出来
	scanf("%s", str);
	printf(str);
}

void input_new() {
	char c = getchar();
	putchar(c);

	c = _getch();
	putchar(c);

	c = getchar();
	putchar(c);

}
