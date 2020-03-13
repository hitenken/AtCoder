N = int(input())
for i in range(N, 1000):
    a = str(i)
    if a[0] == a[1] and a[1] == a[2]:
        print(a)
        exit()