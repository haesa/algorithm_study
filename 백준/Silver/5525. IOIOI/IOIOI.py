import sys
read = sys.stdin.readline

N = int(read())
M = int(read())
S = read()

'''
1: IOI
2: IOIOI
3: IOIOIOI
4: IOIOIOIOI
5: IOIOIOIOIOI
6: IOIOIOIOIOIOI
7: IOIOIOIOIOIOIOI
'''

result = 0
pattern_count = 0
i = 0
while i < M - 2:
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':
        pattern_count += 1
        if pattern_count == N:
            result += 1
            pattern_count -= 1
        i += 2
    else:
        pattern_count = 0
        i += 1

print(result)
