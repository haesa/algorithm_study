input = input()
numbers = input.split(' ')
sum = 0

for n in numbers:
    sum += int(n) ** 2
    
print(sum % 10)