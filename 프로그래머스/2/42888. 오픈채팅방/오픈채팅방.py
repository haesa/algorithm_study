'''
cmd uid nickname



필요한 데이터
- [유저 아이디, Enter or Leave] record
- {유저 아이디: 최종 닉네임}
'''

def solution(record):
    answer = []
    queue = []
    nicknames = {}
    for r in record:
        line = r.split(' ')
        
        cmd = line[0]
        uid = line[1]

        if cmd == 'Enter' or cmd == 'Leave':
            queue.append([cmd, uid])
        if cmd == 'Enter' or cmd == 'Change':
            nicknames[uid] = line[2]

    for q in queue:
        cmd, uid = q
        
        if cmd == 'Enter':
            answer.append(f'{nicknames[uid]}님이 들어왔습니다.')
        elif cmd == 'Leave':
            answer.append(f'{nicknames[uid]}님이 나갔습니다.')
    
    return answer    
