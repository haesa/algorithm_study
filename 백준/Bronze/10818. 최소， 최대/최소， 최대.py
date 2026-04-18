n = input()
numbers = input().split(' ')
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(min(numbers), max(numbers))
    