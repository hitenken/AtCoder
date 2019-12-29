K, X = map(int, input().split())
S = X -(K-1)
while True:
    if S > X + (K -1):
        break
    print(str(S)+" ", end="")
    S += 1