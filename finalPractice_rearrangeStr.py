input1=input()
temp=[]
a=0

count=0

for i in input1:
    print(i)
    if i.isalnum()==True:
        temp.append(i)
res=temp[:]
print(input1,"t",temp,res)

sortFromSmall=sorted(temp)
sortFromLarge=sorted(temp,reverse=True)
print(sortFromLarge,sortFromSmall)
for j in range(len(temp)*2):
    print("j",j)
    if j%2==0:
        print("exif")
        for i in range(len(temp)):
            if res[i]!=sortFromSmall[i]:
                print("problem",i,res[i],sortFromSmall[i])
                count=count+1
                a=res.index(sortFromSmall[i],i)
                res[i],res[a]=res[a],res[i]

                print(res)
                break
    else:
        print("exel")
        for i in range(len(temp)):
            if res[len(temp)-i-1]!=sortFromLarge[i]:
                count=count+1
                retemp=list(reversed(res))
                a=len(res)-retemp.index(sortFromLarge[i],i)-1
                res[len(temp)-i-1],res[a]=res[a],res[len(temp)-i-1]
                print(res)
                break

print(count)