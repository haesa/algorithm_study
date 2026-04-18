#include<stdio.h>
#include<string.h>

int main()
{
	int left, right;
	char word[21];

	scanf("%s", &word);
	
	for (left = 0, right = strlen(word) - 1; left <= right; left++, right--)
	{
		if (word[left] != word[right])
			break;
	}
    
	printf("%s\n", left > right ? "true" : "false");

	return 0;
}