import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

result = []
for num in B:
  pos_left = bisect_left(A, num)
  pos_right = bisect_right(A, num)
  
  result.append(pos_right - pos_left)
  
write(' '.join(map(str, result)))