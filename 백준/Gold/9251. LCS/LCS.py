import sys
read = sys.stdin.readline

str1 = read().rstrip()
str2 = read().rstrip()

len1 = len(str1)
len2 = len(str2)
DP = [[0] * (len2 + 1) for _ in range(len1 + 1)]


for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i - 1] == str2[j - 1]:
            DP[i][j] = DP[i - 1][j - 1] + 1
        else:
            DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])

print(DP[len1][len2])
