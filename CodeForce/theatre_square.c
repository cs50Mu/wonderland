#include <stdio.h>

int main(int argc, char *argv[])
{
	long long  n,m,a;
	long long num = 1;

	scanf("%lld%lld%lld", &n, &m, &a);


	if(n % a != 0) {
		num *= n/a + 1;
	} else
	{
		num *= n/a;
	}

	if(m % a != 0) {
		num *= m/a + 1;
	} else
	{
		num *= m/a;
	}

	printf("%lld\n", num);
	return 0;

}	
