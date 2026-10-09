'''
핵심
- 출력에는 Enter/Leave 기록만 필요하다.
- 최종 닉네임을 사용해야 한다.

필요한 데이터
- Enter/Leave 이벤트 순서
- uid별 최종 닉네임

자료구조
- events: [(cmd, uid), ...]
- nicknames: {uid: nickname}

풀이
1. record를 순회한다.
2. Enter/Leave는 events에 저장한다.
3. Enter/Change는 nicknames를 갱신한다.
4. events를 순회하며 최종 닉네임으로 문장을 만든다.
'''

def solution(record):
    answer = []
    events = []
    nicknames = {}
    for r in record:
        line = r.split(' ')
        
        cmd = line[0]
        uid = line[1]

        if cmd == 'Enter' or cmd == 'Leave':
            events.append([cmd, uid])
        if cmd == 'Enter' or cmd == 'Change':
            nicknames[uid] = line[2]

    for e in events:
        cmd, uid = e
        
        if cmd == 'Enter':
            answer.append(f'{nicknames[uid]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(f'{nicknames[uid]}님이 나갔습니다.')
    
    return answer    
