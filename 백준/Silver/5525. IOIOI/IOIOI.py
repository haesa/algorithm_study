import sys
read = sys.stdin.readline

N = int(read())
M = int(read())
S = read()

'''input
1
13
OOIOIOIOIIOII
'''

'''output
4
'''

pn = [''] * (N + 1)
pn[1] = 'IOI'
for i in range(2, N + 1):
    pn[i] = pn[i - 1] + "OI"


count = 0
i = 0
while True:
    i = S.find(pn[N], i)
    if i == -1:
        break
    count += 1
    i += 1
print(count)
