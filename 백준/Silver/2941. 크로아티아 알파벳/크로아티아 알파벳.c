#include <stdio.h>
#include<string.h>

int main()
{
	char croatia[101];
	int count = 0;
	int i;

	scanf("%s", &croatia);
	for (i = 0; i < strlen(croatia)-1; i++)
	{
		if (croatia[i] == 'c')
		{
			if (croatia[i + 1] == '=')
				i++;
			else if (croatia[i + 1] == '-')
				i++;
		}
		else if (croatia[i] == 'd')
		{
			if (croatia[i + 1] == '-')
				i++;
			else if (croatia[i + 1] == 'z')
				if (croatia[i + 2] == '=')
					i += 2;
		}
		else if (croatia[i] == 'l' || croatia[i] == 'n')
		{
			if (croatia[i + 1] == 'j')
				i++;
		}
		else if (croatia[i] == 's' || croatia[i] == 'z')
		{
			if (croatia[i + 1] == '=')
				i++;
		}
		count++;
	}
	if (i == (strlen(croatia) - 1))
		count++;
	printf("%d\n", count);

	return 0;
}