#include<stdio.h>
#include<math.h>

int main()
{
	int num[2], snum[2] = { 0 };

	scanf("%d %d", &num[0], &num[1]);
	for (int i = 0; i < 2; i++)
	{
		for (int j = 2; j >= 0; j--)
		{
			snum[i] += (num[i] % 10) * pow(10, j);
			num[i] /= 10;
		}
	}
	printf("%d\n", snum[0] > snum[1] ? snum[0] : snum[1]);

	return 0;
}