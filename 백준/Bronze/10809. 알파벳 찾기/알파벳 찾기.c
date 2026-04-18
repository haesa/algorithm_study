#include<stdio.h>

int main()
{
	char word[101];
	char* wp = &word;
	int check[26];

	for (int i = 0; i < 26; i++)
		check[i] = -1;

	scanf("%s", &word);

	for (int i = 0; *wp != '\0'; wp++, i++)
	{
		if (check[*wp - 'a'] != -1)
			continue;

		check[*wp - 'a'] = i;
	}

	for (int i = 0; i < 26; i++)
		printf("%d ", check[i]);

	printf("\n");
	return 0;
}