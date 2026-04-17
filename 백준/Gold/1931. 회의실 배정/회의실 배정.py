import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
schedule_list = []

# 스케줄 입력
for i in range(N):
    schedule = list(map(int, sys.stdin.readline().split()))
    schedule_list.append(schedule)

# 정렬
schedule_list.sort(key = lambda x: (x[1], x[0]))

prevMeetingEnd = 0
result = 0
for i in range(N):
    if schedule_list[i][0] >= prevMeetingEnd:
        result += 1
        prevMeetingEnd = schedule_list[i][1]

write(str(result))
