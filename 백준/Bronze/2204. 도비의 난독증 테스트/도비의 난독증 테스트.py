while True:
  n = int(input())
  if(n == 0):
    break
  words = {}
  for i in range(n):
    word = input()
    words[word.lower()] = word
  result = sorted(words.keys())
  print(words[result[0]])