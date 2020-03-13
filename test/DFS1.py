#n個の配列aの部分和がkになるか判定

def dfs(i, sums, n, k):
    if i == n: return sums == k
    if dfs(i+1, sums,n,k): return True
    if dfs(i+1, sums+a[i],n,k): return True
    return  False

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    if dfs(0,0,n,k):print("Yes")
    else: print("No")