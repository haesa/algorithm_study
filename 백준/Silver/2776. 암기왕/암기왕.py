t = int(input())

for i in range(t):
  n = input()
  n_input = input()
  n_set = set(map(int, n_input.split(" ")))

  m = input()
  m_input = input()
  m_list = list(map(int, m_input.split(" ")))

  for num in m_list:
    if num in n_set:
      print(1)
    else:
      print(0)