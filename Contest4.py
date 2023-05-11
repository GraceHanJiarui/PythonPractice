input1=input().split()
#print(input1)
#print(input1[0][0])
n=len(input1)
#print(n)
li=[]
result=0
for i in range(n):
    a=input1[i][0]
    li.append(int(a))
    b=input1[i][1]
    li.append(int(b))
#print(li)
ma=max(li)
#print(ma)
EmptyList=[[0 for i in range(ma)] for j in range(ma)]

for i in range(n):
    a=input1[i][0]
    b=input1[i][1]
    EmptyList[int(a)-1][int(b)-1]=1

#print(EmptyList)
empli=[]
for i in range(ma):
    #print("i",i)
    for j in range(ma):
        #print("j",j)
        if EmptyList[i][j]==1:
            for x in range(ma):
                #print("x",x)
                if x!=i and x!=j and i!=j:
                    if EmptyList[j][x]==1:
                        #print(i)
                        #print(j)
                        #print(x)
                        #print((i+1)*100+(j+1)*10+x+1)
                        result=result+(i+1)*100+(j+1)*10+x+1
print(result)
