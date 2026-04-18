n, k = [int(x) for x in input().split(' ')]

numbers = [x for x in range(2, n + 1)]

result = 0
count = 0
while count < k:
  min_value = min(numbers)
  max_value = max(numbers)
  for value in range(min_value, max_value + 1, min_value):
    if value in numbers:
      numbers.remove(value)
      count += 1
      if count == k:
        result = value
        break
  if count == k:
    break
  
print(result)