import re

p = re.compile('[ABCDEF]?A+F+C+[ABCDEF]?$')
n = int(input())

result = []
for i in range(n):
  s = input()
  m = p.match(s)
  if m:
    result.append('Infected!')
  else:
    result.append('Good')

for r in result:
  print(r)