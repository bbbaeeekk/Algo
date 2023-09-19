A,B,C = map(int,input().split())

def fpow(A,B,C):
    if B>1:
        x = fpow(A,B//2,C)
        if B%2 == 0:
            return x*x%C
        else:
            return x*x*A%C
    else:
        return A%C
    
print(fpow(A,B,C))
