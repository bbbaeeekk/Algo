word = input()

answer = [-1]*26
arr = []

for x in range(len(word)):
    if word[x] not in arr:
        answer[ord(word[x])-97] = x
        arr.append(word[x])

print(*answer)