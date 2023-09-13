import sys
input = sys.stdin.readline

N = int(input())


## union집단의 수
## 부모가 없으면 내가 부모
## 두집단의 부모에게 1+자식의 수를 추가 하는 리스트 생성
## dict?
## 부모가 같으면 더하지않음
def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    arr = sorted([x,y])
    parent[arr[0]] = arr[1]
    count_set[arr[1]] += count_set[arr[0]]
    return    

for _ in range(N):
    F = int(input())

    count_set={}
    parent={}

    for _ in range(F):
        A, B = input().split()

        if A not in parent:
            parent[A]=A
            count_set[A]=1
        if B not in parent:
            parent[B]=B
            count_set[B]=1 
            
        union(A,B)

        print(count_set[find(A)])