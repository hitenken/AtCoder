def koyaku(A, B):
    ans = []
    for i in range(1,A+1):
        if A%i == 0 and B%i == 0:
            ans.append(i)    
    return ans
if __name__ == "__main__":
    A, B, K = map(int, input().split())
    if B > A:
        tmp = A
        A = B
        B = tmp
    ans = koyaku(A, B)
    print(ans[-K])