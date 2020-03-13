N = int(input())
W = [input() for i in range(N)]
dic = {W[0]:1}
rev = W[0][len(W[0])-1:]
for w in W[1:]:
    if w not in dic:
        dic[w] = 1
        if rev != w[0]:
            print("No")
            exit()
        rev = w[len(w)-1:]
        continue
    print("No")
    exit()
print('Yes')