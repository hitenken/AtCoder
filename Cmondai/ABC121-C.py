N, M = map(int, input().split())
AB = [[int(i) for i in input().split()]for j in range(N)]
sortsecond = lambda val: val[0]
AB.sort(key=sortsecond)
ans = 0
c = 0
for ab in AB:
    if c+ab[1] <= M:
        ans += (ab[0] *ab[1])
        c += ab[1]
        continue
    else:
        while c != M:
            c += 1
            ans += ab[0] 
        break

print(ans)