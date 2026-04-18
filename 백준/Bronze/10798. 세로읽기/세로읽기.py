words = []

for i in range(5):
  words.append(input())

result = []

for i in range(15):
  for j in range(5):  
    if(len(words[j]) < i + 1):
      continue
    result.append(words[j][i])

print(''.join(result))