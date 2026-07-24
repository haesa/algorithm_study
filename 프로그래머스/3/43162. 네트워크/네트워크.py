from collections import deque

def solution(n, computers):
    def bfs(start):
        q = deque([start])
        visited[start] = 1

        while q:
            v = q.popleft()

            for u in range(n):
                if computers[v][u] and not visited[u]:
                    q.append(u)
                    visited[u] = 1
                
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if visited[i]:
            continue
            
        bfs(i)
        answer += 1
    
    return answer


            
        
            