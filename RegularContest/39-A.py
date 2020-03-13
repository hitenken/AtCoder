A, B = map(str, input().split())
ans = -900
for i in range(1, 10):
    tmp = A
    A = str(i) + A[1:]
    ans = max(ans, int(A) - int(B))
    A = tmp
for j in range(2, len(A) + 1):
    for i in range(0, 10):
        tmp = A
        A = A[:j-1] + str(i) + A[j:]
        ans = max(ans, int(A) - int(B))
        A = tmp

for i in range(1, 10):
    tmp = B
    B = str(i) + B[1:]
    ans = max(ans, int(A) - int(B))
    B = tmp
for i in range(0, 10):
    for j in range(2, len(A) + 1):
        tmp = B
        B = B[:j-1] + str(i) + B[j:]
        ans = max(ans, int(A) - int(B))
        B = tmp
print(ans)