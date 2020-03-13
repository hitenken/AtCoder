"""
N 個の足場があって、i 番目の足場の高さは hi です。
最初、足場 1 にカエルがいて、ぴょんぴょん跳ねながら足場 N へと向かいます。カエルは足場
i にいるときに

    足場 i から足場 i+1 へと移動する (そのコストは |hi−hi+1|)
    足場 i から足場 i+2 へと移動する (そのコストは |hi−hi+2|)
    ...
    足場 i から足場 i+Kへと移動する (そのコストは |hi−hi+K|)

のいずれかの行動を選べます。カエルが足場 1 から足場 Nへと移動するのに必要な最小コストを求めよ
"""
def chmin(a, b):
    if a > b:
        a = b
    return a

N, K = map(int, input().split())
hi = list(map(int, input().split()))

dp = [10 ** 10 for i in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(1, K + 1):
        chmin(dp[i + j], dp[i] + abs(hi[i] - hi[i + j]))

print(dp[N-1])