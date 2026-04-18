numbers = []
for i in range(9):
  numbers.append(int(input()))
  
sub = sum(numbers) - 100
result = []
for i in range(9):
  for j in range(9):
    if i == j:
      continue
    if numbers[i] + numbers[j] == sub:
      result = [x for index, x in enumerate(numbers) if index != i and index != j]

for x in result:
  print(x)