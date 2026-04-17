import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# 블루레이 개수 계산
def fn(bluelay_size):
  num = 0
  sum = 0
  
  if max(lectures) > bluelay_size:
    return 0
  
  for size in lectures:
    if sum + size > bluelay_size:
      num += 1
      sum = 0
    sum += size

  return num + 1

def binary_search(array):
  start, end = max(array), sum(array)
  
  while start <= end:
    mid = (start + end) // 2
    
    if fn(mid) <= m:
      end = mid - 1
    else:
      start = mid + 1
    
  return start

print(binary_search(lectures))