#include<stdio.h>

int main() {
	long long fibo[91] = { 0 };
	int n;

	fibo[0] = 0;
	fibo[1] = 1;

	do{
		scanf("%d", &n);
	} while (n > 90);

	for (int i = 2; i <= n; i++)
		fibo[i] = fibo[i - 1] + fibo[i - 2];
	
		printf("%lld\n", fibo[n]);

	return 0;
}