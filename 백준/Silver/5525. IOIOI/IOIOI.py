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

pn = 'IOI' + 'OI' * (N - 1)

count = 0
i = 0
l = len(pn)
while S[i:i+l]:
    if pn == S[i:i+l]:
        i += 2
        count += 1
    else:
        i += 1
print(count)
