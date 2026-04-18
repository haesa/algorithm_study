import sys

input = sys.stdin.readline

N = int(input())

person_list = list(map(int, input().split()))
person_list.sort()

result = 0
for i in range(N):
  result += person_list[i] * (N - i)
  
print(result)
