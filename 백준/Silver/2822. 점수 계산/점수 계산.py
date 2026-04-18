import sys

input = sys.stdin.readline
write = sys.stdout.write

score_list = []
for i in range(8):
  score_list.append(int(input()))

sorted_score_list = sorted(enumerate(score_list), key = lambda x: x[1], reverse = True)

total_score = 0
p_number_list = []
for i in range(5):
  total_score += sorted_score_list[i][1]
  p_number_list.append(sorted_score_list[i][0] + 1)

p_number_list.sort()
write(str(total_score) + '\n' + ' '.join(list(map(str, p_number_list))))