target = input()
word = input()
result = 0

replace = target.replace(word, '#')

for c in replace:
  result = result + 1 if c == '#' else result

print(result)