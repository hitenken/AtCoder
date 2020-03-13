def euclid(a,b):
	if b>a:
		a = b
	return b, a%b

def gcd(a,b):
	while b != 0:
		a,b = euclid(a,b)
	return a

a = int(input())
b = int(input())

lcm = (a*b)/gcd(a,b)
print(lcm)
