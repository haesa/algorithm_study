import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 이진 탐색
def binary_search(list, target):
  start = 0
  end = len(list) - 1
  
  while start <= end:
    mid = (start + end) // 2
    
    if list[mid] > target:
      end = mid - 1
    elif list[mid] < target:
      start = mid + 1
    else:
      return 1
  
  return 0

A.sort()

result = []
for num in B:
  result.append(binary_search(A, num))

write('\n'.join(map(str, result)))