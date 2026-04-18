#include <stdio.h>
#include <math.h>

int d(int n);

int main()
{
	int selfNum[10001];
	int n;

	for (int i = 0; i < 10001; i++)
		selfNum[i] = 0;

	for (int i = 1; i <= 10000; i++)
	{
		if (selfNum[i] == 1)
			continue;
		for (int j = i; d(j) <= 10000; j = d(j))
		{
			n = d(j);
			selfNum[n] = 1;
		}
	}

	for (int i = 1; i <= 10000; i++)
	{
		if (selfNum[i] == 0)
			printf("%d\n", i);
	}

	return 0;
}

int d(int n)
{
	int d = n;

	for (int j = log10(n) + 1; j > 0; j--)
	{
		d += n % 10;
		n /= 10;
	}

	return d;
}