from itertools import product

def solution(users, emoticons):
    emoticon_rate_product = product([10, 20, 30, 40], repeat=len(emoticons))
    mapped_emoticons = [[[a, b] for a, b in zip(emoticons, p)] for p in emoticon_rate_product]
    
    answer = []
    for mapped_emoticon in mapped_emoticons:
        total_amount_list = list(map(lambda x: [x[1], get_total_amount(x[0], x[1], mapped_emoticon)], users))
        
        answer.append(calculate(total_amount_list))
    
    answer.sort(reverse=True)
    
    return answer[0]

def calculate(total_amount_user_list):
    join = 0
    amount = 0
    for limit, total in total_amount_user_list:
        if total >= limit: # 플러스 가입
            join += 1
        else:
            amount += total
    
    return [join, amount]
    
def get_total_amount(user_rate_treshold, user_amount_treshold, emoticons):
    emoticon_paids = list(map(lambda x: get_discount_cost(x[0], x[1]) if x[1] >= user_rate_treshold else 0, emoticons))
    
    return sum(emoticon_paids)
    

def get_discount_cost(emoticon_cost, emoticon_discount_rate):
    return emoticon_cost * (100 - emoticon_discount_rate) * 0.01
    
# 1. 출력
#   1순위: 이모티콘 플러스 가입자 수 최대화
#   2순위: 가입자 수가 같다면 판매액 최대화

# 2. 출력을 만들기 위해 꼭 기억해야 하는 상태
#   [한 가지 할인 정책이 정해졌다고 가정]
# 
#   각 사용자에 대해
#       - 현재 구매 금액은 얼마인가?
#       - 최종적으로 구매자인가, 플러스 가입자인가?

# 3. 문제에서 일어나는 ‘연산’을 한 줄씩 추출
#   1. 각 이모티콘의 할인율을 선택한다.

#   2. 정해진 할인율을 기준으로 각 사용자를 확인한다.
#       - 사용자가 구매할 이모티콘인지 판단한다.
#       - 구매한다면 할인된 가격을 구매 금액에 누적한다.

#   3. 사용자의 총 구매 금액을 기준으로
#       - 플러스 가입 여부를 판단한다.

#   4. 모든 사용자의 결과를 합쳐
#       - 플러스 가입자 수
#       - 총 판매액
#       을 계산한다.
