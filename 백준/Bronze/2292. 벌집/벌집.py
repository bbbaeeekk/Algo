N = int(input())
if N == 1:
    print(1)
else:
    n = int(((N-2)/3)**0.5)
    X = 2+n*(n+1)*3
    if N < X:
        print(n+1)
    else:
        print(n+2)