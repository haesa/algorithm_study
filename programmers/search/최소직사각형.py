def solution(sizes):
    long = []
    short = []
    for size in sizes:
        a, b = size
        long.append(max(a, b))
        short.append(min(a, b))
    
    return max(long) * max(short)