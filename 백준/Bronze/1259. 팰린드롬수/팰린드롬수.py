from collections import deque

def palindrome(number):
  queue = deque(list(number))
  while len(queue) > 1:
    a = queue.popleft()
    b = queue.pop()
    if a != b:
      return 'no'
  return 'yes'  

numbers = []

while True:
  number = input()
  if number == '0':
    break
  numbers.append(number)

result = map(lambda x: palindrome(x), numbers)
print('\n'.join(result))