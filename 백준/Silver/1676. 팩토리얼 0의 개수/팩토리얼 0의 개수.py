N = int(input())

def facto(x):
    n = 1
    for t in range(1,x+1):
        n*=t
    return str(n)

f = facto(N)
cnt = 0
for i in range(len(f)-1,-1,-1):
    if int(f[i]) == 0:
        cnt+=1
    else:
        break
print(cnt)