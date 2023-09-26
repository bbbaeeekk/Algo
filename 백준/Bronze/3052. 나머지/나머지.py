s = set()

for _ in range(10):
    A = int(input())
    a = A%42
    s.add(a)

print(len(s))