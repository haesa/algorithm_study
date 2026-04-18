#include<stdio.h>

int main() {
	int A, B, V;
	int day;

	scanf("%d %d %d", &A, &B, &V);
	if ((V - A) % (A - B) == 0)
		day = (V - A) / (A - B) + 1;
	else
		day = (V - A) / (A - B) + 2;
	
	printf("%d\n", day);
	return 0;
}