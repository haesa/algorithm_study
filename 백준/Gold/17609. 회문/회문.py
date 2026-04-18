def palindrome(word):
  return word == word[::-1]

def check_pseudo_palindrome(word):
  i = 0
  j = len(word) - 1
  
  while i < j:
    if word[i] != word[j]:
      if word[i+1] == word[j] or word[i] == word[j-1]:
        if palindrome(word[:i] + word[i + 1:]) or palindrome(word[:j] + word[j + 1:]):
          return True
        else:  
          return False
    i += 1
    j -= 1

n = int(input())

for _ in range(n):
  s = input()
  if palindrome(s):
    print(0)
  elif check_pseudo_palindrome(s):
    print(1)
  else:
    print(2)
