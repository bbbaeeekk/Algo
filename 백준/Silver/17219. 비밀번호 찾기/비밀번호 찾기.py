import sys
input = sys.stdin.readline

N, M = map(int,input().split())

saved = {}
for _ in range(N):
    site, password = input().split()
    saved[site] = password

for _ in range(M):
    sites = input().strip()
    print(saved[sites])