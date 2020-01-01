N, K, Q = map(int, input().split())
point = [K - Q for i in range(N)]
A = [int(input()) for j in range(Q)]

for num in A:
    point[num-1] += 1

for num in point:
    if num > 0:
        print('Yes')
        continue
    print('No')
    