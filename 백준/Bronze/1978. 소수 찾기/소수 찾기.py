N = int(input())
arr = list(map(int,input().split()))

sosu = [True]*1001
sosu[1] = False
for i in range(2,int(1000**0.5)+1):
    for j in range(i*i,1001):
        if j%i == 0:
            sosu[j] = False
cnt = 0
for x in arr:
    if sosu[x]:
        cnt += 1

print(cnt)