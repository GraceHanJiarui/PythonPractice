def Queen(i,j):
    for di in range(8):
        if isOccupied(di,j)==True and di!=i:
            break
        qipan[di][j]=1
    for dj in range(8):
        if isOccupied(i,dj)==True and dj!=j:
            break
        qipan[i][dj]=1
    for dx in range(8):
        if dx!=0:
            if i+dx<8 and j-dx>=0:
                if isOccupied(i+dx,j-dx)==True:
                    break
                qipan[i+dx][j-dx]=1
    for dx in range(8):
        if dx!=0:
            if i+dx<8 and j+dx<8:
                qipan[i+dx][j+dx]=1
    for dx in range(8):
        if dx!=0:
            if i-dx>=0 and j-dx>=0: 
                qipan[i-dx][j-dx]=1
    for dx in range(8):
        if dx!=0:
            if i-dx>=0 and j+dx<8:
                qipan[i-dx][j+dx]=1


def Car(i,j):
    for di in range(8):
        if isOccupied(di,j)==True and di==i:
            break
        qipan[di][j]=1
    for dj in range(8):
        if isOccupied(i,dj)==True and dj==j:
            break
        qipan[i][dj]=1

def B(i,j):
        for dx in range(8):
            if i+dx<8 and j-dx>=0:
                if qipan[i+dx][j-dx]!=5:
                    qipan[i+dx][j-dx]=1
                else:
                    break
        for dx in range(8):
            if i+dx<8 and j+dx<8:
                if qipan[i+dx][j+dx]!=5:
                    qipan[i+dx][j+dx]=1
                else:
                    break
        for dx in range(8):
            if i-dx>=0 and j-dx>=0: 
                if qipan[i-dx][j-dx]!=5:
                    qipan[i-dx][j-dx]=1
                else:
                    break
        for dx in range(8):
            if i-dx>=0 and j+dx<8:
                if qipan[i-dx][j+dx]!=5:
                    qipan[i-dx][j+dx]=1
                else:
                    break

def isOccupied(i,j):
    if qipan[i][j]==5:
        return True
    return False

input1=input().split()
qizi=["Q","R","B","P","N"]
dingwei=["a","b","c","d","e","f","g","h"]
qipan=[[0 for i in range(8)] for j in range(8)]
for i in input1:
    if i[0]=="K":
        row=dingwei.index(i[1])
        col=8-int(i[2])
    else:
        a=qizi.index(i[0])
        qipan[8-int(i[2])][dingwei.index(i[1])]=5
print(qipan)
for i in input1:
    a=qizi.index(i[0])
    if a==0:
        Queen(8-int(i[2]),dingwei.index(i[1]))
    elif a==1:
        Car(8-int(i[2]),dingwei.index(i[1]))
    elif a==2:
        B(8-int(i[2]),dingwei.index(i[1]))
print(qipan)