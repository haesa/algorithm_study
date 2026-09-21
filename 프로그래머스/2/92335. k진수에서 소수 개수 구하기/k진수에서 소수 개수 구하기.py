'''
1. n을 k진수로 변환 (string)
2. 0이 연속되는 구간을 구분자로 삼고 split
4. int로 매핑
5. 소수 판단 -> 소수인 요소만 배열에 남기기
6. 배열 개수 반환
'''

def solution(n, k):
    answer = 0
    # 진법 변환 (타입: 문자열)
    value = convert_base(n, k)
    
    # 0이 연속되는 구간 기준으로 나누기
    for x in value.split('0'):
        if x == '':
            continue
        if is_prime(int(x)):
            answer += 1
    return answer

def convert_base(value, base):    
    result = ''
    while value:
        result += str(value % base)
        value //= base
    return result[::-1]

def is_prime(value):
    if value < 2: return False
    k = 2
    while k * k <= value:
        if value % k == 0: return False
        k += 1
    return True