N, L = map(int, input().split())
num = [i for i in range(L,N+L)]
min = 10000
index = 0
for i in range(N):
    if min > abs(num[i]):
        min = abs(num[i])
        index = i

print(sum(num)-num[index])  