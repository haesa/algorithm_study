alpha = [-1] * 26
s = input()

for i in range(len(s)):
  if alpha[ord(s[i]) - 97] != -1:
    continue
  alpha[ord(s[i]) - 97] = i

result = map(lambda x: str(x), alpha)
print(' '.join(list(result)))