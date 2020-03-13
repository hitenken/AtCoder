# how to confirm if there is key in dict
N = int(input())
S = {}
for i in range(N):
    s = input()
    if s not in S: # key is not in dict
        S[s] = 1
        continue
    S[s] +=1
    

