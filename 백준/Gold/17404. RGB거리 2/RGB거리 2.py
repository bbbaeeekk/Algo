N = int(input())

House = [list(map(int,input().split())) for _ in range(N)]

take = [[0,1,2],[1,0,2],[2,0,1]]

min_list = []

for x in range(3):
    X = take[x]
    min_price = [0]*N
    min_price[0] = House[0][X[0]]
    min_price[1] = [min_price[0] + House[1][X[1]],min_price[0] + House[1][X[2]]]

    if N >= 3:
        min_price[2] = [min_price[0] + House[1][X[2]] + House[2][X[1]], min_price[0] + House[1][X[1]] + House[2][X[2]]]

    if N >= 4:
        for y in range(3,N):
            min_price[y] = [0,0]  
            min_price[y][0] = min(min_price[y-1][1]+House[y][X[1]], min(min_price[y-2]) + House[y-1][X[0]] + House[y][X[1]]) 
            min_price[y][1] = min(min_price[y-1][0]+House[y][X[2]], min(min_price[y-2]) + House[y-1][X[0]] + House[y][X[2]])

    min_list.append(min_price[-1][0])
    min_list.append(min_price[-1][1])

print(min(min_list))
