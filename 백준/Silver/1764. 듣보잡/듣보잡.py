nm = input()
n,m = map(int, nm.split(' '))

a = set()
for i in range(n): 
  a.add(input())

b = set()
for i in range(m):
  b.add(input())

result = list(a & b)
result.sort()
    
print(len(result))
for c in result:
  print(c)