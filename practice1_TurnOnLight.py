input1=input().split()
res=set()
def turn(i,j):
    if i<8 and j<8 and i>=0 and j>=0:
        if mat[i][j]==0:
            mat[i][j]=1
        elif mat[i][j]==1:
            mat[i][j]=0

mat=[[0 for i in range(8)] for j in range(8)]
int(input1[0])
for i in range(1,int(input1[0])+1):
    a=input1[i]
    row=int(a[0])
    for j in range(1,len(a)):
        mat[8-row][int(a[j])-1]=1
press=[]
dingwei=int(input1[0])+1
pressNum=int(input1[dingwei])
print(pressNum)
for i in range(dingwei+1,len(input1)):
    b=input1[i]
    pressedrow=int(b[0])
    for j in range(1,len(b)):
        press.append((8-pressedrow,int(b[j])-1))
for x,y in press:
    print("ex",x,y)
    turn(x,y)
    turn(x+1,y)
    turn(x+2,y)
    turn(x-2,y)
    turn(x-1,y)
    turn(x,y+1)
    turn(x,y+2)
    turn(x,y-1)
    turn(x,y-2)
    turn(x+1,y+1)
    turn(x-1,y-1)
    turn(x+1,y-1)
    turn(x-1,y+1)

print(mat)
count=0
for i in range(8):
    for j in range(8):
        if mat[i][j]==1:
            count+=1
print(count)