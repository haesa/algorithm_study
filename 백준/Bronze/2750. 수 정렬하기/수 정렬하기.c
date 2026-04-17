#include<stdio.h>
int main()
{
	int sort[1000], n;
	int min;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf(" %d", &sort[i]);

	for (int i = 0; i < n - 1; i++)
	{
		for (int j = i + 1; j < n; j++)
			if (sort[i] > sort[j])
			{
				min = sort[j];
				sort[j] = sort[i];
				sort[i] = min;
			}
	}

	for (int i = 0; i < n; i++)
		printf("%d\n", sort[i]);

	return 0;
}