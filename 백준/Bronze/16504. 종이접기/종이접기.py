n = int(input())

numbers = []
for i in range(n):
  numbers += [int(x) for x in input().split(' ')]
  
print(sum(numbers))