import sys

input = sys.stdin.readline

N, P, Q = map(int, input().split())

A = {}
A[0] = 1

def solution(n):
  if n in A:
    return A[n]
  
  A[n] = solution(n // P) + solution(n // Q)
  return A[n]

print(solution(N))
