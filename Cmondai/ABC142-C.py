N = int(input())
A = list(map(int, input().split()))
target = []
for i in range(0, N):
    target.append([A[i], i + 1])

target.sort()

for i in range(0, N):
    print(target[i][1],end=" ")