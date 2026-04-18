#include<stdio.h>
int main()
{
	int time[2], sub;

	scanf("%d %d", time, time + 1);
	if (*(time + 1) >= 45)
		printf("%d %d\n", *time, *(time + 1) - 45);
	else 
	{
		sub = 45 - *(time + 1);
		printf("%d %d\n", *time == 0 ? 23 : *time - 1, 60 - sub);
	}

	return 0;
}