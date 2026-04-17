#include<stdio.h>

int main() {
	long long f1 = 0, f2 = 1, fn;
	int n;

	do{
		scanf("%d", &n);
	} while (n > 90);

    if(n < 2)
        printf("%d\n", n);
    else {
	    for (int i = 2; i <= n; i++) {
	    	fn = f1 + f2;
	    	f1 = f2;
	    	f2 = fn;
	    }
        printf("%lld\n", fn);
    }
		
	return 0;
}