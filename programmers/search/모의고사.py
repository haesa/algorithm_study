one = [1, 2, 3, 4, 5]
two = [2, 1, 2, 3, 2, 4, 2, 5]
three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
my_answer_list = [one, two, three]

def solution(answers):
    result = []
    temp = []
       
    for index, my_answer in enumerate(my_answer_list):
        value = check(answers, my_answer)
        temp.append(value)
    
    max_value = max(temp)
    
    for index, value in enumerate(temp):
        if value == max_value:
            result.append(index + 1)

    return result

def check(answers, my_answer):
    result = 0
    length = len(my_answer)
    for index, answer in enumerate(answers):
        num = my_answer[index % length]
        if answer == num:
            result += 1
    return result