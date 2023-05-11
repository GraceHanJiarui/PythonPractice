i=1
li=[]
dict1={"D":".","I":".","Q":"?","E":"!"}
res=[]
realres=[]

def Find(inpu):
    a=0
    if inpu=="N":
        a=n.pop(0)
    if inpu=="C":
        a= c.pop(0)
    if inpu=="V":
        a= v.pop(0)
    if inpu=="J":
        a= j.pop(0)
    if inpu=="B":
        a= b.pop(0)
    if inpu=="P":
        a= p.pop(0)
    if inpu=="T":
        a="the"
    if inpu=="A":
        a="kong"
    return a

while i >=0:
    temp=input()
    if temp.isdigit()==True:
        i=int(temp)
    else:
        li.append(temp)
        i-=1
# print(li)
sentence=li.pop()
for y in li:
    tempo=y.split()
    # print(y,tempo)
    if tempo[0]=="N":
        n=tempo[1:]*10
    if tempo[0]=="C":
        c=tempo[1:]*10
    if tempo[0]=="V":
        v=tempo[1:]*10
    if tempo[0]=="J":
        j=tempo[1:]*10
    if tempo[0]=="B":
        b=tempo[1:]*10
    if tempo[0]=="P":
        p=tempo[1:]*10
sentenceli=sentence.split(" ")
for i in sentenceli:
    sentenceType=dict1[i[0]]
    for dj in range(1,len(i)):
        # print("j",dj)
        res.append(Find(i[dj])[:])
    if sentenceType=="?":
        res.insert(0,"what")
    for i in range(len(res)-1):
        if res[i]=="kong":
            # print("res[i+1][0]",res[i+1][0])
            if res[i+1][0] in ["a","e","i","o","u"]:
                # print("ex")
                res[i]="an"
                # print(res,res[i])
            else:
                res[i]="a"
    realres.append(" ".join(res[:])+sentenceType)
    # print(res,realres)
    res=[]
ret=""
for i in realres:
    a=i.capitalize()
    ret=ret+a+" "
print(ret)