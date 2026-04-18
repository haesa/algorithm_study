def getScoreSum(ox):
  k = 0
  score = 0
  for c in ox:
    if c == 'O':
      k += 1
      score += k
    else:
      k = 0
  return score

n = int(input())
scores = []

for i in range(n):
  scores.append(input())

result = list(map(lambda x: getScoreSum(x), scores))
for score in result:
  print(score)
