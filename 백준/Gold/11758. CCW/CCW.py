p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))

V1 = [p2[0]-p1[0],p2[1]-p1[1]]
V2 = [p3[0]-p2[0],p3[1]-p2[1]]

cp = V1[0]*V2[1]-V1[1]*V2[0]

if cp == 0:
    print(0)
elif cp > 0:
    print(1)
elif cp < 0:
    print(-1)