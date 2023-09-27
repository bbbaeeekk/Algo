import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, n = int(input()), int(input())

    apart = [[]]
    for i in range(n+1):
        apart[0].append(i)

    for j in range(1,k+1):
        apart.append([])
        for l in range(n+1):
            cnt = 0
            for m in range(l+1):
                cnt += apart[j-1][m]
            apart[j].append(cnt)

    print(apart[k][n])