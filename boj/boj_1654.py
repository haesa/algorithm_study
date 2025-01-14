k, n = map(int, input().split(' '))

lan_list = []
for _ in range(k):
  lan = int(input())
  lan_list.append(lan)

def binary_search(value):
  start, end = 1, value
  
  while start <= end:
    mid = (start + end) // 2  # 랜선 절단 단위 길이
    num = 0 # 랜선 개수
    for lan in lan_list:
      num += lan // mid
    
    if num >= n:
      start = mid + 1
    else:
      end = mid - 1
  print(end)

min_value = max(lan_list)
binary_search(min_value)
