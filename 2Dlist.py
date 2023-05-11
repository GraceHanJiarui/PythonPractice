li=[[0 for i in range(8)] for j in range(8)]
input1=input().split()
result=0
weishu=int(input1[0])
print(input1[1:weishu+1],"weishu")
for i in input1[1:weishu+1]:
    li[int(i[0])-1][int(i[1])-1]=not li[int(i[0])-1][int(i[1])-1]
    if len(i)>=3:
        li[int(i[0])-1][int(i[2])-1]=not li[int(i[0])-1][int(i[2])-1]
    print(li,"li")
    
dengshu=int(input1[weishu+1])
for i in input1[weishu+2:]:
    try:
        li[int(i[0])-1][int(i[1])-1]= not li[int(i[0])-1][int(i[1])-1]
    except Exception:
        pass
    
    try:
        li[int(i[0])][int(i[1])-1]=not li[int(i[0])][int(i[1])-1]
    except Exception:
        pass

    try:
        li[int(i[0])+1][int(i[1])-1]=not li[int(i[0])+1][int(i[1])-1]
    except Exception:
        pass
    
    try:
        li[int(i[0])-2][int(i[1])-1]=not li[int(i[0])-2][int(i[1])-1]
    except Exception:
        pass
    
    try:
        li[int(i[0])-3][int(i[1])-1]=not li[int(i[0])-3][int(i[1])-1]
    except Exception:
        pass
    
    try:
        li[int(i[0])-1][int(i[1])]=not li[int(i[0])-1][int(i[1])]
    except Exception:
        pass
    
    try:
        li[int(i[0])-1][int(i[1])+1]=not li[int(i[0])-1][int(i[1])+1]
    except Exception:
        pass
    
    try:
        li[int(i[0])][int(i[1])]=not li[int(i[0])][int(i[1])]
    except Exception:
        pass
        
    try:
        li[int(i[0]-2)][int(i[1])]=not li[int(i[0]-2)][int(i[1])]
    except Exception:
        pass
    
    try:
        li[int(i[0])-1][int(i[1])-2]=not li[int(i[0])-1][int(i[1])-2]
    except Exception:
        pass

    print(li)
    if len(i)>=3:
        li[int(i[0])-1][int(i[2])-1]= not li[int(i[0])-1][int(i[2])-1]
    print(li,"liiiiii")


for i in li:
    if i ==1 or True:
        result=result+1

print(result)

"""
        
turnon=input1[1]
turnoff=input1[2]
xlocation=input1[3]
li[int(turnon[0])-1][int(turnon[1])-1]=1
if turnon[2]:
    li[int(turnon[0])-1][int(turnon[2])-1]=1
print(li)
    """

#elif int(input[0])==2:
