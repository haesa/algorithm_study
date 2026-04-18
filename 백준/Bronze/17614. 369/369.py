def include369(number_str):
  return any(sub in number_str for sub in ['3', '6', '9'])

def count369(number_str):
  count = 0
  for char in number_str:
    count += (1 if include369(char) else 0)
  return count

result = 0
n = int(input())

for i in range(n):
  number = i + 1
  number_str = str(number)
  if include369(number_str):
    result += count369(number_str)
    
print(result)