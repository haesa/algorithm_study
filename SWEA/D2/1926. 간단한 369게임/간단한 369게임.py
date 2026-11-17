N = int(input())

for n in range(1,N + 1):
    s = str(n)
    if '3' in s or '6' in s or '9' in s:
        cnt = s.count('3') + s.count('6') + s.count('9')
        print('-' * cnt, end = ' ')
    else:
        print(s, end=' ')