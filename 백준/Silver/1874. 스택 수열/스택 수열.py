N = int(input())

flag = True
n = 0
stack = []
answer = []
for _ in range(N):
    K = int(input())
    while flag:

        if stack and K == stack[-1]:
            answer.append('-')
            del stack[-1]
            break
        
        n += 1
        if n > N:
            flag = False
            break
        stack.append(n)
        answer.append('+')


if flag:
    for x in answer:
        print(x)
else:
    print('NO')
        