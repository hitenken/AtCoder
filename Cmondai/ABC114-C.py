def get3sin(x):
    if x // 3 == 0:
        l.insert(0,x%3)
        return 
    l.insert(0,x%3)
    return get3sin(x//3)

N = input()
ans = 0
henkan = {'7':0, '5':1, '3':2}

for i in range(3, len(N)+1):
    for j in range(3 ** i):
        l = []
        get3sin(j)
        
        for n, val in enumerate(l):
            if val == 0:
                l[n] = 7
            elif val == 1:
                l[n] = 5
            else:
                l[n] = 3
        
        cnt = [False for i in range(3)]
        for i in l:
            cnt[henkan[str(i)]] = True
        judge = True
        for i in range(3):
            if not cnt[i]:
                judge = False
        if not judge:
            continue
        if int(''.join(map(str, l))) <= int(N):
            ans += 1
        
print(ans)
        
                               
        