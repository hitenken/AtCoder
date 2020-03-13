
def solve(x):
    x = str(x)
    if len(x) != N:
        return False
    for s, c in P:
        if x[s - 1] != str(c):
            return False
    return True

if __name__ == "__main__":
    N, M = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(M)]
    ans = 10**N
    for i in range(10 ** N - 1, -1, -1):
        if solve(i):
            ans = min(ans, i)
            
    print(ans if ans != 10**N else -1)