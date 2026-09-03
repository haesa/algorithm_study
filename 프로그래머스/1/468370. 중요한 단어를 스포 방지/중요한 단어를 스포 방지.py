'''
출력: 스포 방지 단어 집합에 대한 일반 단어 차집합의 크기
필요한 데이터: 스포 방지 단어 집합(spoiler), 일반 단어 집합(normal)
'''

def solution(message, spoiler_ranges):
    spoiler = set()
    normal = set()
    
    ws = 1 if message[0] == ' ' else 0
    i = 0
    
    while ws < len(message):
        # [ws, we) 형태로 단어 찾기
        we = ws + 1
        
        while we < len(message) and message[we] != ' ':
            we += 1
        word = message[ws:we]
        
        # 현재 단어보다 앞에 있는 스포 구간 제거
        while i < len(spoiler_ranges) and spoiler_ranges[i][1] < ws:
            i += 1
            
        if i < len(spoiler_ranges):
            # 단어 구간 [ws, we)
            # 스포 구간 [ss, se]
            ss, se = spoiler_ranges[i]
            if se >= ws and we > ss: # 스포일러 구간 겹치는 경우
                spoiler.add(word)
            else:
                normal.add(word)
        else:
            normal.add(word)
        
        # 다음 단어
        ws = we + 1
            
    return len(spoiler - normal)