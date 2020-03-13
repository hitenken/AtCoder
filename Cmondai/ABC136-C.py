N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
count = 0
for i in range(1, N):
    if H[i] > H[i - 1]:
        H[i] -= 1 

for i in range(1, N):
    if H[i] <H[i - 1]:
        print("No")
        exit()
print("Yes")