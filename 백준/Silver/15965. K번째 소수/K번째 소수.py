MAX = 7400000
k = int(input())

numbers = [1 for _ in range(MAX)]
result = []

for i in range(2, MAX):
  if(numbers[i] == 1):
    result.append(i)
    for j in range(i + i, MAX, i):
      numbers[j] = 0

print(result[k - 1])