esm = list(map(int, input().split(' ')))

for x in range(0, 7980):
  if x % 15 == esm[0] - 1 and x % 28 == esm[1] -1 and x % 19 == esm[2] -1:
    print(x + 1)
    break