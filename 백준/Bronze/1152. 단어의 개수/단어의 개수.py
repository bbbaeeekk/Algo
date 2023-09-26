sep = input()
cnt=0

flag=False
for x in range(len(sep)):
    if sep[x] != ' ':
        if  flag==False:
            cnt+=1
        flag=True
    elif sep[x] == ' ':
        flag=False
        
print(cnt)