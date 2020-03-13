N = int(input())
S = {}
for i in range(N):
    s = input()
    if s not in S:
        S[s] = 1
        continue
    S[s] +=1
    

M = int(input())
T = {}
for i in range(M):
    t = input()
    if t not in T:
        T[t] = 1
        continue
    T[t] += 1

ans = 0
for key in S.keys():
    if key not in T:
        ans = max(ans, S[key])
        continue
    ans = max(ans, S[key] - T[key])
print(ans)