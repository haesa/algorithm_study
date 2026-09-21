'''
1. n을 k진수로 변환 (string)
2. 0이 연속되는 구간을 구분자로 삼고 split
4. int로 매핑
5. 소수 판단 -> 소수인 요소만 배열에 남기기
6. 배열 개수 반환
'''

import math
import re

def solution(n, k):
    # 진법 변환 (타입: 문자열)
    value = convert_base(n, k)
    
    # 0이 연속되는 구간 기준으로 나누기
    value_list = re.split(r'0+', value)
    
    # 맨 오른쪽 끝에 0이 있는지 확인 후 전처리
    if value_list[-1] == '':
        value_list = value_list[:-2]
    
    # 소수만 남기기
    prime_list = [x for x in list(map(int, value_list)) if is_prime(x)]
    
    return len(prime_list)

def convert_base(value, base):    
    result = ''
    
    while value >= base:
        value, remainder = divmod(value, base)
        result += str(remainder)
        
    result += str(value)
    return result[::-1]

def is_prime(value):
    if value < 2:
        return False
    
    for k in range(2, math.isqrt(value) + 1):
        if value % k == 0:
            return False
    
    return True