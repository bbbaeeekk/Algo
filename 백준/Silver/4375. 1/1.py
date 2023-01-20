while 1:
    try:
        n = int(input())
    except:
        break

    a = 1

    while a % n:
        a = a*10 + 1

    print(len(str(a)))