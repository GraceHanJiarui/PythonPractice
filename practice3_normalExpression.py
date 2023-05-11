import  re
li=[]
n=6
while n!=0:
    try:
        m = input()
        li.append(m)
        n-=1
    except:
        break

print(li)
s=li[0].split(",")
print(s)
temp=[]
res=[None for i in range(5)]
for i in range(1,6):
    for j in s:
        print(j,"".join(re.findall(li[i],j)))
        if j=="".join(re.findall(li[i],j)):
            print("ex")
            temp.append(j)
            print(temp)
    res[i-1]=temp[:]
    temp=[]
print(res)

