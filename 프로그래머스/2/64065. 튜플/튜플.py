'''
문자열 파싱
    - 양 끝 중괄호 삭제
    - },{ 기준 split
    - 배열 순회하며 문자열 -> 배열 매핑
    - 원소 개수 올림차순 정렬
    - 원소 형변환 (string -> number)
'''

def solution(s):
    # 양 끝 이중 중괄호 제거 {{, }}
    string = s[2:-2]
    
    # 중간 중괄호 제거 및 배열 매핑
    arr_list = string.split('},{')
    
    # 배열로 매핑 & 원소 개수 오름차순 정렬
    arr_list = list(map(lambda x: x.split(','), arr_list))
    arr_list.sort(key=lambda x: len(x))
    
    answer = []
    
    for arr in arr_list:
        for element in arr:
            element_int = int(element) # 형변환 (string -> number)
            if element_int in answer:
                continue
            else:
                answer.append(element_int)
    
    return answer

