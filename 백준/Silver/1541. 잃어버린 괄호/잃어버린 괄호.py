import sys
import re
read = sys.stdin.readline

expr = read().rstrip()


def get_sum(expr):
    result = 0
    nums = re.split(r'[+\-]', expr)

    for n in nums:
        result += int(n)

    return result


if '-' in expr:
    first_minus_pos = expr.index('-')
    first = get_sum(expr[:first_minus_pos])
    second = get_sum(expr[first_minus_pos + 1:])

    print(first - second)
else:
    print(get_sum(expr))
