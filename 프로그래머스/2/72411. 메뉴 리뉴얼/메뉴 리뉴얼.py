'''
- course 개수 별 각 order의 조합 구하기
- 코스 조합 등장 빈도 카운트
- 빈도가 가장 높은 것 선택
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        menus = []
        for order in orders:
            for combi in combinations(sorted(order), c):
                menus.append(''.join(combi))
        
        counter = Counter(menus)
        if not counter:
            continue
            
        max_count = max(counter.values())
        
        list = [
            menu
            for menu, count in counter.items()
            if max_count >= 2 and count == max_count
        ]
        answer.extend(list)
    
    answer.sort()
    return answer