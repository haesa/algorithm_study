import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())

def star(n):
  if n == 1:
    return '*'
  
  prev_pattern = star(n // 3)
  pattern = []
  
  for p in prev_pattern:
    pattern.append(p * 3)
  for p in prev_pattern:
    pattern.append(p + ' ' * (n // 3) + p)
  for p in prev_pattern:
    pattern.append(p * 3)
  
  return pattern

pattern = star(N)
write('\n'.join(pattern))