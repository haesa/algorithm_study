n = int(input())
str = []
for i in range(n):
  str.append(input())
  
def is_group_word(word):
  check = []
  for c in word:
    if c not in check:
      check.append(c)
    elif check[-1:][0] != c:
      return False
  return True
      
group_words = list(map(lambda x: is_group_word(x), str))
result = list(filter(lambda x: x, group_words))
print(len(result))