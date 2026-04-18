#include<stdio.h>

int calc(int n1, int n2, char op);

int main()
{
	int k1, k2, k3, result1, result2;
	char o1, o2;

	scanf("%d %c %d %c %d", &k1, &o1, &k2, &o2, &k3);

	result1 = calc(k1, k2, o1);
	result1 = calc(result1, k3, o2);

	result2 = calc(k2, k3, o2);
	result2 = calc(k1, result2, o1);

	if (result1 < result2)
		printf("%d\n%d\n", result1, result2);
	else
		printf("%d\n%d\n", result2, result1);

	return 0;
}

int calc(int n1, int n2, char op)
{
	int num;

	if (op == '+')
		num = n1 + n2;
	else if (op == '-')
		num = n1 - n2;
	else if (op == '*')
		num = n1 * n2;
	else if (op == '/')
		num = n1 / n2;

	return num;
}