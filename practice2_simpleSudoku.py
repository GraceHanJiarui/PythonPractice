input1=input().split(",")
mat=[["" for i in range(4)] for i in range(4)]
for i in range(4):
    row=int((int(input1[i])-6)/6)
    col=int((int(input1[i])-6)%6)-2
    mat[row][col]="1"
start=5
while start<len(input1)-1:
    temp=int(input1[start+1])
    if temp<7:
        for i in range(4):
            if mat[i][temp]!="1":
                mat[i][temp]=input1[start]
                break
    elif temp>31:
        for i in range(4):
            if mat[3-i][temp%6-2]!="1":
                mat[3-i][temp%6-2]=input1[start]
                break
    elif temp==7 or temp==13 or temp==19 or temp==25:
        for i in range(4):
            if mat[int(temp/6)-1][i]!="1":
                mat[int(temp/6)-1][i]=input1[start]
                break
    elif temp==12 or temp==18 or temp==24 or temp==30:
        for i in range(4):
            if mat[int((temp-1)/6)-1][3-i]!="1":
                mat[int((temp-1)/6)-1][3-i]=input1[start]
                break
    start+=2

def backTrack(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]=="":
                for x in ("A","B","C"):
                    if x not in mat[i] and x not in (mat[y][j] for y in range(4)):
                        mat[i][j]=x
                        if backTrack(mat):
                            return True
                        mat[i][j]=""
                return False
    return True
backTrack(mat)
print(mat)