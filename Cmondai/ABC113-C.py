N, M = map(int, input().split())
l = []
cnt = [0 for i in range(N+1)]//県の個数
k_id = [0 for i in range(M)]//市の個数
for i in range(M):
    P, Y = map(int, input().split())
    l.append([Y, P , i])
l.sort(key=lambda x: x[0])
for i in range(M):
    y, p, idx = l[i][0], l[i][1], l[i][2]
    cnt[p] += 1
    k_id[idx] = [p, cnt[p]]
for i in range(M):
    print(str(k_id[i][0]).zfill(6)+str(k_id[i][1]).zfill(6))