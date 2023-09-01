import sys

y, z = map(int,sys.stdin.readline().split())

double = [0] * 55
double[1] = 1

for x in range(2,55):
    double[x] = 2**(x-1) + 2*double[x-1]

def counts(a):
    global flag
    cnt = 1
    while True:
        k = 2**cnt - 1
        if k == a:
            return cnt
        if k > a:
            cnt -=1
            return cnt
        cnt +=1

def fnt(n):
    finalcnt = 0
    while 1:
        cntt = counts(n)  ## 2의 제곱승
        n -= (2**cntt -1)  ## 원래수 - 직전 정수
        finalcnt += (double[cntt] + n)

        if n == 0:
            return finalcnt
        n -= 1
        if cntt == 0:
            return finalcnt
        

print(fnt(z)-fnt(y-1))