N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
X = 0
Y = 0
for i in range(N):
  if ans < (X + V[i]) - (Y + C[i]):
      X += V[i]
      Y += C[i]
      ans = X - Y

print(ans)