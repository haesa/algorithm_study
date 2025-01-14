def binary_search(list, target):
  left, right = 0, len(list) - 1
  
  while left <= right:
    mid = (left + right) // 2
    if list[mid] == target:
      return 1
    elif list[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return 0
  
t = int(input())

for i in range(t):
  n = input()
  n_input = input()
  n_list = sorted(map(int, n_input.split(" ")))

  m = input()
  m_input = input()
  m_list = list(map(int, m_input.split(" ")))

  for num in m_list:
    print(binary_search(n_list, num))