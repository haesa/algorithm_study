def include369(number_str):
  return number_str == '3' or number_str == '6' or number_str == '9'

result = 0
n = int(input())
for i in range(1, n + 1):
  for c in str(i):
    if include369(c):
      result += 1
      
print(result)