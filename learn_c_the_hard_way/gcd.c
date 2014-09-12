#include <stdio.h>

int gcd(int a, int b)
{
	if(a % b == 0) return b;

	return gcd(b, a%b);
}

int main(int argc, char *argv[])
{
	int a = atoi(argv[1]);
	int b = atoi(argv[2]);

	printf("The Greatest Common Divisor of %d and %d is: %d\n", a, b, gcd(a, b));
}

