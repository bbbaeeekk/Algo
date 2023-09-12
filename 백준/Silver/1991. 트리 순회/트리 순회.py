N = int(input())

tree = {}
for _ in range(N):
    node = list(input().split())
    tree[node[0]] = [node[1],node[2]]

def preorder(x):
    if x == '.':
        return
    print(x, end='')
    preorder(tree[x][0])
    preorder(tree[x][1])
    return

def inorder(x):
    if x == '.':
        return
    inorder(tree[x][0])
    print(x, end='')
    inorder(tree[x][1])
    return

def postorder(x):
    if x == '.':
        return
    postorder(tree[x][0])
    postorder(tree[x][1])
    print(x, end='')
    return

preorder('A')
print()
inorder('A')
print()
postorder('A')