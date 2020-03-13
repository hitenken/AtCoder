def isPrime(N):
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

def isPrime2(N):
    N = str(N)
    ans = [int(i) for i in N]
    if int(N[-1]) % 2 != 0 and int(N[-1]) != 5 and sum(ans) % 3 != 0:
        return True
    return False


N = int(input())

if N == 1:
    print("Not Prime")

elif isPrime(N):
    print("Prime")

elif isPrime2(N):
    print("Prime")
else:
    print("Not Prime")