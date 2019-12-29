N = int(input())
p = list(map(int, input().split()))
p_t = [i for i in range(1, N+1)]
count = 0
for i in range(N):
    if p[i] != p_t[i]:
        count += 1

if count == 2 or count == 0:
    print('YES')
else:
    print('NO')