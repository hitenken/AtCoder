H, W = map(int, input().split())
S = []
for i in range(H):
    s = list(input())
    for j in range(W):
        if s[j] == '.':
            s[j] = 0
    S.append(s)

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        for k in range(8):
            nx = j + dx[k]
            ny = i + dy[k]
            if nx >= 0 and ny >= 0 and ny < H and nx < W :
                if S[ny][nx] == "#":
                    S[i][j] += 1
for i in range(H):
    l = map(str,S[i])
    ans = "".join(l)
    print(ans)