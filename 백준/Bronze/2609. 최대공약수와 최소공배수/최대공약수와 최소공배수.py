a, b = [int(x) for x in input().split(' ')]

def gcd(a, b):
  while b > 0:
    a, b = b, a % b
  return a
  
gcd_val = gcd(a, b)
print(gcd_val, int(a * b / gcd_val))