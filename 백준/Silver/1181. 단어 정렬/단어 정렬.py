n = int(input())
s = set()

for i in range(n):
  s.add(input())

words = list(s)
result = sorted(words, key = lambda x: (len(x), x) )

for word in result:
  print(word)