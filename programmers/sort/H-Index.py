def solution(citations):
    citations.sort(reverse=True)
    return max(list(map(min, enumerate(citations, start=1))))
    