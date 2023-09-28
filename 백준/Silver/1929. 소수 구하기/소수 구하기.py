M, N = map(int, input().split())

def eratosthenes(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아니므로 제외
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve

# M이상 N이하의 소수를 찾아 출력
sieve = eratosthenes(N)
for i in range(M, N + 1):
    if sieve[i]:
        print(i)
