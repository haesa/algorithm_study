n, m = [int(x) for x in input().split(' ')]
a = set()
b = set()

for i in range(n):
  a.add(input())

for i in range(m):
  b.add(input())

s = a & b
result = list(s)
result.sort()
print(len(result))
print('\n'.join(result))