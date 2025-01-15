import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
dots = list(map(int, input().split(' ')))
dots.sort()

def binary_search_lower_bound(dots, target):
  start, end = 0, len(dots) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if dots[mid] == target:
      return mid
    elif dots[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  return start
      
def binary_search_uppder_bound(dots, target):
  start, end = 0, len(dots) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if dots[mid] == target:
      return mid
    elif dots[mid] < target:
      start = mid + 1
    else:
      end = mid - 1

  return end

for _ in range(m):
  left, right = map(int, input().split())
  print(binary_search_uppder_bound(dots, right) - binary_search_lower_bound(dots, left) + 1)
