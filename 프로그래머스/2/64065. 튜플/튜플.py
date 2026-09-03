'''
문자열 파싱
    - 양 끝 중괄호 삭제
    - },{ 기준 split
    - 배열 순회하며 문자열 -> 배열 매핑
    - 원소 개수 올림차순 정렬
    - 원소 형변환 (string -> number)
'''

def solution(s):
    # 문자열 파싱
    s1 = s[2:-2].split('},{')
    
    # 배열 매핑 & int 형변환
    tuple_set_list = []
    for s in s1:
        tuple_set_list.append(list(map(int, s.split(','))))
        
    # 원소 개수 올림차순 정렬
    tuple_set_list.sort(key=lambda x: len(x))
    
    answer = []
    
    for tuple_set in tuple_set_list:
        for element in tuple_set:
            if element not in answer:
                answer.append(element)
    
    return answer

