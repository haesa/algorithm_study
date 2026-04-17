import sys
input = sys.stdin.readline

n = int(input())
ph_list = list(map(int, input().split()))
ph_list.sort()

result = []
min = 2_000_000_000
for i in range(n - 1):
  start, end = i + 1, n - 1

  while start <= end:
    mid = (start + end) // 2
    
    if abs(ph_list[i] + ph_list[mid]) < min:
      min = abs(ph_list[i] + ph_list[mid])
      result = [ph_list[i], ph_list[mid]]
        
    if (ph_list[i] + ph_list[mid]) == 0:
      break
    elif (ph_list[i] + ph_list[mid]) < 0:
      start = mid + 1
    else:  
      end = mid - 1

result.sort()
print(" ".join(map(str, result)))