from math import sqrt

def next_prime(x):
    i = 2
    while i*i <= x:
        if x % i == 0:
            return True
        i += 1
    return False

x = int(input())
while next_prime(x):
      x = x + 1

print(x)