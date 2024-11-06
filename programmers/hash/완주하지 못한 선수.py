# key를 선수 이름으로 두고, value를 동일한 이름을 가진 인원 수로 두어 풀이했다.
# participant 리스트를 순회하여 dict에 해당 이름을 가지고 있는 인원 수 저장하고,
# completion 리스트를 순회하여 동일한 이름에 대해서 value를 1 감소시켰다.
# 이때 value가 1인 item이 딱 하나 존재하게 된다.
# participant에서 completion을 뺐을 때 value가 1이라는 건 완주하지 못 했다는 의미이므로
# value가 1인 item에 대한 key를 반환하면 된다.

hash = dict()

def solution(participant, completion):    
    for name in participant:
        hash[name] = hash.get(name, 0) + 1
    for name in completion:
        hash[name] = hash.get(name) - 1

    for key, value in hash.items():
        if value == 1:
            return key