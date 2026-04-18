n = int(input())
coords = []
for i in range(n):
    mn = input().split(' ')
    mn = [int(x) for x in mn]
    coords.append(mn)
    
coords.sort(key=lambda x: (x[0], x[1]))
for m, n in coords:
    print(m, n)