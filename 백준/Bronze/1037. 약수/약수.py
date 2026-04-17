n = int(input())
numbers = [int(x) for x in input().split(' ')]
print(min(numbers) * max(numbers))