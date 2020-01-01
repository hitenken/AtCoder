import math 
def is_prime(x):
    j = 2
    while(j <= math.sqrt(x)):
        if x % j == 0:
            return False
        j += 1
    return True
    
    
x = int(input())

while (not is_prime(x)):
     x += 1
    
print(x)
