S = input()
ans = 0
if S[0] == '1':
    for i in range(1, len(S)):
        if i % 2 == 0:
            if S[i] != '1':
                ans += 1
        else:
            if S[i] != '0':
                ans += 1
    print(ans)
else:
    for i in range(1, len(S)):
        if i % 2 == 0:
            if S[i] != '0':
                ans += 1
        else:
            if S[i] != '1':
                ans += 1
    print(ans)      