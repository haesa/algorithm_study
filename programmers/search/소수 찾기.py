from itertools import permutations

def solution(numbers):
    prime_set = set()
    length = len(numbers)
    
    for k in range(1, length + 1):
        for perm in permutations(numbers, k):
            number = int(''.join(perm))
            
            if number in prime_set:
                continue
                
            if isPrime(number):
                prime_set.add(number)

    return len(prime_set)

def isPrime(number):
    if number == 0 or number == 1:
        return False
    
    for k in range(2, int(number ** 0.5) + 1):
        if number % k == 0:
            return False
    return True