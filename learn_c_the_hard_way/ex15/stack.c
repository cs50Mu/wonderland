#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <assert.h>

#define STACKSIZE 1000


void die(const char *message) {
	if (errno) {
		perror(message);
	}
	else {
		printf("ERROR: %s\n", message);
	}

	exit(1);
}


typedef struct {
	int size;
	int items[STACKSIZE];
} STACK;

void push(STACK *ps, int x)
{
	if(ps->size == STACKSIZE)
	
		die("Error: stack overflow\n");
	
	else
	
	ps->items[ps->size++] = x;
	
}

int pop(STACK *ps)
{
	if(ps->size == 0)
	
		die("Error: stack underflow\n");
	
	else
	
		return ps->items[--ps->size];
}


int main(int argc, char *argv[])
{
//	int i;
	STACK *stack = malloc(sizeof(STACK)); // 初始化
	stack->size = 0;

	push(stack, 30);

	assert(30 == pop(stack));


	free(stack);    // 记得free啊！

	return 0;
}
