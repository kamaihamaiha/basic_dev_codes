#include <iostream>

int main()
{
   
	// sizeof integer
	printf("sizeof char: %d\n", sizeof(char));
	printf("sizeof short: %d\n", sizeof(short));
	printf("sizeof int: %d\n", sizeof(int));
	printf("sizeof float: %d\n", sizeof(float));
	printf("sizeof double: %d\n", sizeof(double));
	printf("sizeof long: %d\n", sizeof(long));
	printf("sizeof long long: %d\n", sizeof(long long));

	// sizeof var
	int a = 1;
	printf("sizeof var int a: %d\n", sizeof(a));

	// size of const
	printf("sizeof const 1: %d\n", sizeof(1));
}

