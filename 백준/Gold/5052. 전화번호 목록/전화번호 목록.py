import sys
read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N = int(read())
    numbers = sorted([(read().strip()) for _ in range(N)])
    flag = True
    for i in range(N - 1):
        if numbers[i + 1].startswith(numbers[i]):
            flag = False
            break
    print('YES' if flag else 'NO')
