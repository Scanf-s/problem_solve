import sys
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b) # 최소 공배수

def solve():
    N, M, x, y = map(int, sys.stdin.readline().split())
    
    x -= 1
    y -= 1
    
    limit = lcm(N, M)
    current = x
    
    while current < limit:
        if current % M == y:
            return current + 1
        current += N
    
    return -1 

T = int(sys.stdin.readline().strip())
for _ in range(T):
    print(solve())

