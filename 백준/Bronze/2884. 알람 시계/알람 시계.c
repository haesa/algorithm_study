#include<stdio.h>
int main()
{
	int hour, min;

	scanf("%d %d", &hour, &min);

	if (min >= 45)
		printf("%d %d\n", hour, min - 45);
	else 
		printf("%d %d\n", hour == 0 ? 23 : hour - 1, min + 15);

	return 0;
}