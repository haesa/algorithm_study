'''
1. records의 요소를 배열로 파싱 [입차 시간, 차량 번호, 내역]
2. 주차 시간 계산
- 내역이 'IN'인 경우 입차 내역을 입차 딕셔너리에 추가 { 차랑 번호: 입차 시간 }
- 내역이 'OUT'인 경우 주차 시간 계산 후 주차 시간 딕셔너리에 업데이트 { 차량 번호: 총 주차 시간 }
3. 요금 계산
4. 차량 번호 오름차순 정렬
'''

from collections import defaultdict
import math

def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees
    
    in_dict = {}
    time_dict = defaultdict(int)
    
    # 주차 시간 계산
    for record in records:
        time, car_number, history = record.split(' ')
        
        if history == 'IN':
            in_dict[car_number] = time_to_minutes(time)
        elif history == 'OUT':
            in_time = in_dict.pop(car_number)
            parking_time = time_to_minutes(time) - in_time
            time_dict[car_number] += parking_time
    
    for car_number, in_time in in_dict.items():
        out_time = time_to_minutes('23:59')
        parking_time = out_time - in_time
        time_dict[car_number] += parking_time
    
    # 요금 계산
    answer = []
    for car_number in sorted(time_dict.keys()):
        parking_time = time_dict[car_number]
        extra_time = max(parking_time - default_time, 0)
        extra_fee = math.ceil(extra_time / unit_time) * unit_fee
        answer.append(default_fee + extra_fee)
    
    return answer

def time_to_minutes(time):
    hour, minute = list(map(int, time.split(':')))
    return hour * 60 + minute
