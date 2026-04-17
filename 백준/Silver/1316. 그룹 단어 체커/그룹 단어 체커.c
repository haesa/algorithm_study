#include<stdio.h>
#include<string.h>

int main() {
	int n, count = 0, k;
	int alpha[26];
	char word[101], ch;

	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf(" %s", word);

		for (int j = 0; j < 26; j++)
			alpha[j] = 0;

		for (k = 0; k < strlen(word); k++) {
			ch = word[k];

			if (word[k] != word[k + 1])
				alpha[ch - 97] += 1;

			if (alpha[ch - 97] > 1)
				break;
		}
		if (k == strlen(word)) count++;
	}
	printf("%d\n", count);

	return 0;
}