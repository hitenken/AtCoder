A, B, C = map(int, input().split())
K = int(input())
max_ = max(A, B, C)

print(max_*2**K + A + B + C - max_)