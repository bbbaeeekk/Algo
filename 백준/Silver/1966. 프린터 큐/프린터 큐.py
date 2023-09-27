import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    N, M = map(int,input().split())
    imp = list(map(int,input().split()))
    ind = [0]*N
    for x in range(N):
        ind[x]=x
    imp2, ind2 = [],[]

    rank = 0
    while imp:
        n = imp[0]
        i = ind[0]
        if n >= max(imp):
            ind2.append(i)
        else:
            imp.append(n)
            ind.append(i)
        del imp[0]
        del ind[0]

    print(ind2.index(M)+1)
