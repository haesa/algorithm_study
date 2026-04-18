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

n, m = map(int, input().split(' '))

dots = list(map(int, input().split(' ')))
lines = [list(map(int, input().split(' '))) for _ in range(m)]
dots.sort()

result = []
for line in lines:
  start, end = 0, len(dots) - 1
  
  if line[0] >= dots[0]:
    start = binary_search_lower_bound(dots, line[0])
  if line[-1] <= dots[-1]:
    end = binary_search_uppder_bound(dots, line[-1])
  result.append(end - start + 1)

for num in result:
  print(num)