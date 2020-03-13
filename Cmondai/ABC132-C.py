N = int(input())
d = list(map(int, input().split()))


d.sort()
if d[N // 2] == d[N // 2 - 1]:
    print(0)
    exit()
ans = d[N // 2] - d[N // 2 - 1]
print(ans)