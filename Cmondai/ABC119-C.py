def dfs(d, a, b, c):
    if d == N:#-30は最初の1木目の合体コストがかからないため減算
        return abs(A - a)+abs(B - b)+abs(C - c)-30 if min(a, b, c)>0 else INF
    ans0 = dfs(d + 1, a, b, c)
    ans1 = dfs(d + 1, a + l[d], b, c) + 10
    ans2 = dfs(d + 1, a, b + l[d], c) + 10
    ans3 = dfs(d + 1, a, b, c + l[d]) + 10
    return min(ans0, ans1, ans2, ans3)

if __name__ == "__main__":
    N, A, B, C = map(int, input().split())
    l = [int(input()) for i in range(N)]
    INF = 10**10
    ans = dfs(0, 0, 0, 0)
    print(ans)