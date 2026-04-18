n1, n2 = input().split(' ')
result = max(int(n1[::-1]), int(n2[::-1]))
print(result)