n = int(input())
numbers = [int(x) for x in input().split(' ')]

result = 0
for x in numbers:
  if x == 1:
    continue
  flag = 1
  for i in range(2, x):
    if x % i == 0:
      flag = 0 
      break
  result += 1 if flag == 1 else 0
  
print(result)