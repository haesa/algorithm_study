def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(result(array, command))
    
    return answer

def result(array, command):
    i, j, k = command
    start = i - 1
    end = j
    newArray = array[start:end]
    newArray.sort()
    return newArray[k-1]
