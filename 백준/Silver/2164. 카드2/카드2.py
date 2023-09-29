from collections import deque

N = int(input())

dq = deque([i+1 for i in range(N)])

while len(dq)>1:
    dq.popleft()
    s = dq.popleft()
    dq.append(s)

print(dq[0])