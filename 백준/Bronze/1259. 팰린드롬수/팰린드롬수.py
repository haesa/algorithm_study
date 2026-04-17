from collections import deque

def palindrome(origin):
  rev = ''.join(list(reversed(origin)))
  return 'yes' if rev == origin else 'no'

numbers = []

while True:
  number = input()
  if number == '0':
    break
  numbers.append(number)

result = map(lambda x: palindrome(x), numbers)
print('\n'.join(result))