# 폰켓몬을 중복 없이 최대로 선택할 수 있는 개수는 n / 2
# 매개변수로 전달 받은 nums의 중복을 없앤 후의 요소의 개수를 k라고 할 때,
# 만약 k가 n / 2 보다 작다면 중복 없이 선택할 수 있는 폰켓몬의 최대 개수는 k가 된다.
# 중복이 없는 k개의 폰켓몬을 선택하고 난 후에는 어떤 폰켓몬을 선택해도 중복이 생기기 때문이다.

def solution(nums):
    halfLength = len(nums) // 2
    uniqueLength = len(set(nums))
    
    if halfLength > uniqueLength:
        return uniqueLength
    return halfLength