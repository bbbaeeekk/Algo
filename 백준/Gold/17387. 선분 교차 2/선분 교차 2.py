L1 = list(map(int,input().split()))
L2 = list(map(int,input().split()))




L1a = [L1[0],L1[1]]
L1b = [L1[2],L1[3]]
L2a = [L2[0],L2[1]]
L2b = [L2[2],L2[3]]

def vect(a,b):
    return [b[0]-a[0],b[1]-a[1]]

q = vect(L1a,L1b)
w = vect(L2a,L2b)
qw1 = vect(L1a,L2a)
qw2 = vect(L1a,L2b)
wq1 = vect(L2a,L1a)
wq2 = vect(L2a,L1b)

def cww(v1,v2):
    return v1[0]*v2[1]-v1[1]*v2[0]

if cww(q,qw1)*cww(q,qw2) == 0 and cww(w,wq1)*cww(w,wq2) == 0:
    if L1a[0] < L1b[0]:
        a,b = L1a[0],L1b[0]
    else:
        a,b = L1b[0],L1a[0]
    if L2a[0] < L2b[0]:
        n,m = L2a[0],L2b[0]
    else:
        n,m = L2b[0],L2a[0]

    if L1a[1] < L1b[1]:
        a1,b1 = L1a[1],L1b[1]
    else:
        a1,b1 = L1b[1],L1a[1]
    if L2a[1] < L2b[1]:
        n1,m1 = L2a[1],L2b[1]
    else:
        n1,m1 = L2b[1],L2a[1]

    if (n>b) or (m<a) or (n1>b1) or (m1<a1):
        print(0)
    else:
        print(1)

elif cww(q,qw1)*cww(q,qw2) <= 0 and cww(w,wq1)*cww(w,wq2) <= 0:
    print(1)

else:
    print(0)