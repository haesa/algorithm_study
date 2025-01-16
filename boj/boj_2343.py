import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lectures = list(map(int, input().split()))

# 블루레이 개수 계산
def is_valid_blueray_count(lectures, blueray_size, m):
  if max(lectures) > blueray_size:
    return False
  
  sum = 0
  num = 0
  for size in lectures:
    if sum + size > blueray_size:
      num += 1
      sum = 0
    sum += size

  return (num + 1) <= m

def binary_search(lectures, m):
  start, end = max(lectures), sum(lectures)
  
  while start <= end:
    mid = (start + end) // 2
    
    if is_valid_blueray_count(lectures, mid, m):
      end = mid - 1
    else:
      start = mid + 1
    
  return start

print(binary_search(lectures, m))