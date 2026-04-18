scores = [0] * 20
for i in range(20):
    scores[i] = int(input())

w = scores[:10]
k = scores[10:]
w.sort(reverse=True)
k.sort(reverse=True)

print(sum(w[:3]), sum(k[:3]))