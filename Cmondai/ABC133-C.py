L, R = map(int, input().split())

if R - L >= 2019:
    print(0)
else:
    ans = 10**10
    for i in range(L, R + 1):
        for j in range(i + 1, R + 1):
            ans = min(ans, (i * j) % 2019)
    
    print(ans)