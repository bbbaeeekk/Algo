while 1:
    arr = list(map(int,input().split()))
    if arr == [0,0,0]:
        break
    else:
        arr = sorted(arr)
        a,b,c = arr
        if a**2+b**2 == c**2:
            print('right')
        else:
            print('wrong')