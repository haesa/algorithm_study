T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    result = float('-inf')
    if (N < M):
        for j in range(M - N + 1):
            temp = 0
            for i in range(N):
                temp += A[i] * B[i + j]
            result = max(result, temp)
    else:
        for j in range(N - M + 1):
            temp = 0
            for i in range(M):
                temp += B[i] * A[i + j]
            result = max(result, temp)

    print(f'#{test_case} {result}')
    