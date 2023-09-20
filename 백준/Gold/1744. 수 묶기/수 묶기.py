import sys
input = sys.stdin.readline

N = int(input())

pos = []
neg = []
pN=0
nN=0

answer=0
for i in range(N):
    x = int(input())
    if x == 1:
        answer+=1
    elif x > 1:
        pos.append(x)
        pN+=1
    else:
        neg.append(x)
        nN+=1

pos = sorted(pos)
neg = sorted(neg)

if pN%2:
    answer+=pos[0]
    for x in range(pN-1,1,-2):
        answer+=pos[x]*pos[x-1]
else:    
    for x in range(pN-1,0,-2):
        answer+=pos[x]*pos[x-1]
if nN%2:
    answer+=neg[-1]
    for x in range(0,nN-2,2):
        answer+=neg[x]*neg[x+1]
else:
    for x in range(0,nN-1,2):
        answer+=neg[x]*neg[x+1]

print(answer)