n = int(input())

result = 0
for num in range(1, n + 1):
  num_str = str(num)
  result += num_str.count('3') + num_str.count('6') + num_str.count('9')

print(result)