T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    time = 0
    fish = 0
    for t in arr:
        while time < t:
            time += M
            fish += K

        if time > t:
            time -= M
            fish -= K

        if fish > 0:
            fish -= 1
        else:
            print(f'#{test_case} Impossible')
            break

    if fish > 0:
        print(f'#{test_case} Possible')