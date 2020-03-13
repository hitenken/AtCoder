N, A, B = map(int, input().split())

ans = (N // (A + B)) * A
p = N % (A + B)
print(ans+min(p,A))