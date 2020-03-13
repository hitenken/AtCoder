N = int(input())
a = [int(input()) for i in range(N)]

i = 0
c = 0
while a[i] != 2:
    if a[i] == 0:
        c = -2
        break
    tmp = a[i]
    a[i] = 0
    i = tmp - 1
    c += 1
print(c + 1)