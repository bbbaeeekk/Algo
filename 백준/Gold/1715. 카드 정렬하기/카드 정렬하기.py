import sys
import heapq
input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    x = int(input())
    heapq.heappush(q,x)

cnt = 0
for _ in range(N-1):
    a = heapq.heappop(q)
    b = heapq.heappop(q)
    c = a+b
    cnt+=c
    heapq.heappush(q, c)

print(cnt)