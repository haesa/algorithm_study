from collections import deque

def solution(begin, target, words):
    # early return
    if not target in words:
        return 0

    words_count = len(words)
    visited = [[0] * words_count for _ in range(words_count)] # visited[방문주체][방문대상]
    q = deque([(-1, 0)]) # (방문주체, 방문단계) / -1: begin
    
    # bfs
    while q:
        cur, step = q.popleft()
        cur_word =  begin if cur == -1 else words[cur]
        
        if cur_word == target: # target 도달 시 현재 step 반환
            return step
        
        for i in range(words_count):
            same_count = sum(a == b for a, b in zip(cur_word, words[i]))

            if not visited[cur][i] and same_count == len(cur_word) - 1:
                q.append((i, step + 1))
                visited[cur][i] = 1
