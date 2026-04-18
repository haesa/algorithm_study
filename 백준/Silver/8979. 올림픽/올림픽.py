n, k = [int(x) for x in input().split(' ')]

prize = {}
for i in range(n):
  code, *medal = input().split(' ')
  prize[int(code)] = [int(x) for x in medal]

order = sorted(prize.items(), key = lambda x : (-x[1][0], -x[1][1], -x[1][2]))

rank = [0] * (n + 1)
score = order[0][1]
rank_num = 1
for code, medals in order:
  if medals != score:
    rank_num += 1    
  rank[code] = rank_num
  score = medals

print(rank[k])