t = int(input())

for tc in range(1, 1 + t):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]
    # print(arr)
    dc = [0, 0, 1, -1, 1, 1, -1, -1]
    dr = [1, -1, 0, 0, 1, -1, 1, -1]

    ans = "NO"
    for i in range(n):
        for j in range(n):

            for l in range(8):
                cnt = 0
                for m in range(5):
                    if arr[i][j] == "o":
                        ni = i + dc[l] * m
                        nj = j + dr[l] * m

                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == "o":
                            cnt += 1

                            if arr[ni][nj] == ".":
                                continue
                if cnt >= 5:
                    ans = "YES"

    print(f'#{tc} {ans}')
