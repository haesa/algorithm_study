students = [0] * 31
for _ in range(28):
    code = int(input())
    students[code] = 1

result = []
for i in range(1, 31):
    if students[i] == 0:
        result.append(i)

result.sort()
for k in result:
    print(k)