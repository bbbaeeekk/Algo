import sys
input = sys.stdin.readline

zero = [0]*41
zero[0] = 1
zero[2] = 1
one = [0]*41
one[1:2] = [1,1]

for i in range(3,41):
    zero[i]=zero[i-1]+zero[i-2]
    one[i]=one[i-1]+one[i-2]

N = int(input())
for _ in range(N):

    x = int(input())

    print(zero[x], one[x])