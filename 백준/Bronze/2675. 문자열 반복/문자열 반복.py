N = int(input())

for _ in range(N):
    r,s = input().split()
    for x in s:
        print(x*int(r),end='')
    print()