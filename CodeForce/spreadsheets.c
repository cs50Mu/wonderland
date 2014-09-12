#include <stdio.h>
#include <stdlib.h>

int numeration(char *p);

int numeration(char *p)
{
	if(*p == 'R')
	{
		p++;
		while(*p >= '0' && *p <= '9')
			p++;
		if(*p == 'C' && *(p-1) != 'R')  // 排除RC15这种情况
			return 2;
		else
			return 1;
	}
	else
		return 1;
}


int main(int argc, char *argv[])
{
	int line,i,col,row;
	char cell[100];

	scanf("%d", &line);

	while(line--)
	{
		scanf("%s", cell);

		if(numeration(cell) == 1)
		{
			for(i = 0; i < 100; i++)
			{
				if(cell[i] >= '0' && cell[i] <= '9')
					break;
			}
			
			int key = i;
			col = 0;
			row = 0;
			for(i = 0; i <= key-1; i++)
			{
				col = col*26 + (cell[i] - 'A' + 1) ;
			}
			
			row = atoi(&cell[key]);
			
			printf("R%dC%d\n", row, col);
		}
		else
		{
			for(i = 1; i < 100; i++)
			{
				if(cell[i] == 'C')
					break;
			}

			col = atoi(&cell[i+1]);

			row = atoi(&cell[1]);  // notice here

			char temp[100];
			int mod;
			int p = 0;
			while(col)
			{
				mod = col % 26;
				if(mod == 0) mod = 26;
				temp[p++] = 'A' + mod - 1;
				col--;
				col /= 26;
			}

			for(i = p-1; i >= 0; i--)
			{
				printf("%c", temp[i]);   // print col
			}
			printf("%d\n", row);   // print row

		}
	}

				
}
