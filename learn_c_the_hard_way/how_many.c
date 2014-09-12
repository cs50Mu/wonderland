#include <stdio.h>

int how_many(int a, int number)
{
	int unit = 0;
	int dec = 0;
	int count = 0;
	if(a/10 == 0)
	{
		if(a == number)
		{
			count++;
		}
	}
	else
	{
		unit = a%10;
		dec = a/10;
		if(unit == number)
		{
			count++;
		}
		if(dec == number)
		{
			count++;
		}
	}
	return count;

}

int main(int argc, char *argv[])
{
	int number = atoi(argv[1]);
	int i;
	int count = 0;
	
	for(i=1; i<50; i++)
	{
		count += how_many(i, number);
	
	}

	printf("%d\n",count);

}

