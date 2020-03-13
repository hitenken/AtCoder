A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
N = int(input())
b = [int(input()) for i in range(N)]

for i in b:
    for j in range(3):
        if A1[j] == i:
            A1[j] = 0
        if A2[j] == i:
            A2[j] = 0
        if A3[j] == i:
            A3[j] = 0

flag = False
A = [A1,A2,A3]
for i in range(3):
    if sum(A[i]) == 0:
        flag = True
    sum_ = 0
    for j in range(3):
        sum_ += A[j][i]
    if sum_ == 0:
        flag = True

if A1[0] + A2[1] + A3[2] == 0:
    flag = True
if A1[2] + A2[1] + A3[0] == 0:
    flag = True
print('Yes' if flag else 'No')