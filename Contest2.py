input0=input()
inputt=input0.split(" ")
input1=inputt[0]
likong=[]
MaxLen=int(inputt[1])
longeststr=""
li=[]
finalli=[]
liii=[]
i=0
j=0
x=len(input1)
y=0
q=0
o=0
for i in range(len(input1)-1):

    if input1[i]!=input1[i+1]:
        li.append(input1[j:i+1])
        j=i+1
        print("lii",li)
        o=0
    else:
        o=o+1
li.append(input1[-o-1:])

sortedLi=sorted(li)
print("li",li)
print("sortedLi",sortedLi)
while x>1:
    res=max(sortedLi,key=len,default="")
    if res:
        finalli.append(res)
        print(finalli)
        sortedLi.remove(res)
        x=x-1
        print(res)
    else:
        break
finallistr="".join(finalli)
print(finallistr)

for i in range(len(finallistr)-1):

    if finallistr[i]!=finallistr[i+1]:
        likong.append(finallistr[y:i+1])
        y=i+1
likong.append(finallistr[i+1:])

print(likong,"likong")

while q<len(likong):
    res=max(likong,key=len,default="")
    print(len(res))
    if len(res)>MaxLen:
        a=likong.index(res)
        likong[a]=res[:MaxLen]
    q=q+1
print("".join(likong))
