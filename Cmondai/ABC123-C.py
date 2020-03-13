import math

N = int(input())
l = [int(input()) for i in range(5)]
min_ = min(l)
g = math.ceil(N/min_)
print(4+g)