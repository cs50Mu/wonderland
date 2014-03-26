#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int id = atoi(argv[1]);
	int size = sizeof(id);
	printf("%d\n%d\n", size, id);
	
	return 0;
}
