import sys

t = int(sys.stdin.readline())
for _ in range(t):
  heights = []
  input()
  for n in sys.stdin.readline().strip().split(' '):
    heights.append(int(n))
    heights.sort()
    
  level = []
  i = len(heights) - 1
  level.append(abs(heights[i] - heights[i - 1]))
  level.append(abs(heights[1] - heights[0]))
  while i > 1:
    level.append(abs(heights[i] - heights[i - 2]))
    i -= 1
  
  print(max(level))