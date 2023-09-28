import sys
input = sys.stdin.readline

N = int(input())
counting = [0]*10001

for _ in range(N):
    n = int(input())
    counting[n] += 1

for x in range(10001):
    if counting[x]>0:
        for _ in range(counting[x]):
            print(x)