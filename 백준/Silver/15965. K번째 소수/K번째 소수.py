MAX = 7400000
k = int(input())
prime = [True] * MAX
prime[0] = prime[1] = False

count = 0
for i in range(2, MAX):
  if prime[i]:
    count += 1
    if count == k:
      print(i)
      break
    for j in range(i + i, MAX, i):
      prime[j] = False