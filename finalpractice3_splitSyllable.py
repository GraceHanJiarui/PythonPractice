input1=input()
inputTemp=input1[:]
inputResult=input1[:]
vowels=['a','e','i','o','u']
comboCon=["ch",'ck','sh','ph','th','wh','wr']
prefix=['co','de','dis','pre','re','un']
suffix=['age','ful','ing','less','ment']
pre=[]
suf=[]
mid=[]

for i in prefix:
    a=input1.find(i)
    while a==0:
        pre.append(input1[:len(i)])
        input1=input1[len(i):]
        a=input1.find(i)
print(input1,"p",pre)

for i in suffix:
    b=input1.find(i)
    while b+len(i)==len(input1):
        suf.insert(0,input1[b:])
        input1=input1[:b]
        b=input1.find(i)
print(input1,"s",suf)
i=0


while i <len(input1):
    print("ex")
    if input1[i] not in vowels:
        if input1[i:i+2] in comboCon:
                i=i+2
                continue
        else:
            mid.append(input1[:i])
            input1=input1[i:]
            i=1
    else:
        i=i+1
    print(mid,"input1:",input1,"i:",i,"len",len(input1))

print("end",mid,"input1:",input1,"i:",i,"len",len(input1))
mid.append(input1)
if mid[0]=="" or mid[-1]=="":
    mid.remove("")
z=0
for j in vowels:
    if j in mid[0]:
        z=z+1
if z==0:
    mid[1]="".join([mid[0],mid[1]])
    mid.pop(0)
    print(mid)
i=1
z=0
while i<len(mid):
    for j in vowels:
        if j in mid[i]:
            z=z+1
    if z==0:
        mid[i]="".join([mid[i-1],mid[i]])
        mid.pop(i-1)
        print(mid)
    else:
        i=i+1
    z=0