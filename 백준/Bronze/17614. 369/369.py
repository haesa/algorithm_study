n = int(input())

result = 0
for num in range(1, n + 1):
  for c in str(num):
    if c == '3' or c == '6' or c == '9':
      result += 1
      
print(result)