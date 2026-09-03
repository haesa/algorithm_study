'''
출력: 스포 방지 단어 리스트 중 중복 제거하고, 평문(스포 구간 X)에 나온 적 없는 단어의 개수
필요한 데이터: 스포 방지 단어 리스트, 스포 구간이 아닌 단어 리스트

- 스포 구간 -> 스포 방지 단어 리스트, 스포 구간이 아닌 단어 리스트 구하기
- 스포 방지 단어 리스트 중복 제거
- 스포 방지 단어 리스트 순회 -> 스포 구간이 아닌 단어 리스트에 포함되지 않으면 카운트
'''

def solution(message, spoiler_ranges):
    prev_end = 0
    spoiler_words = []
    non_spoiler_words = []
    for start, end in spoiler_ranges:
        # 스포 방지 단어 리스트
        while message[start] != ' ' and start > 0:
            start -= 1
        while message[end] != ' ' and end < len(message) - 1:
            end += 1
        
        for word in message[start:end+1].rstrip().split():
            if word not in spoiler_words:
                spoiler_words.append(word)
        
        # 스포 구간이 아닌 단어 리스트
        for word in message[prev_end:start].rstrip().split():
            if word not in non_spoiler_words:
                non_spoiler_words.append(word)
        
        prev_end = end

    # 스포일러 구간 뒤에 message가 남은 경우 처리
    for word in message[prev_end:len(message)].rstrip().split():
        if word not in non_spoiler_words:
            non_spoiler_words.append(word)
        
    answer = 0

    for word in spoiler_words:
        if word not in non_spoiler_words:
            answer += 1

    return answer
