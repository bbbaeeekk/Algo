word = input().upper()

d = {}
for x in word:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1

max_value = max(d.values())
max_keys = [key for key, value in d.items() if value == max_value]

if len(max_keys) > 1:
    print('?')
else:
    print(max_keys[0])