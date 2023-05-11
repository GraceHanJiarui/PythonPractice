import sys
li = []  
list1 = []
res=[]
i=0
emptyLi=[]
minValue=0
for line in sys.stdin:    
    list1 = line.split()
    li.extend(list1)


heng=int(li[1])
shu=int(li[0])
new_li=li[2:]

liA=new_li[0:heng*shu]
liB=new_li[heng*shu:heng*shu*2]
liC=new_li[heng*shu*2:]
##print(liA,liB,liC)

while (i%heng!=0 & shu*(heng-1)-i>=0 )| i ==0:
    ##print("start")


    maxValue=max(liA[i+1],liA[i+heng],liB[i+1],liB[i+heng],liC[i+1],liC[i+heng])
    #print(maxValue,"maxValue",type(liA[i+1]))
    minValue=minValue+int(min(liA[i],liB[i],liC[i]))
    #print(minValue,"minValue")
    rightL=i+1
    downL=heng+1
    for j in liA[i+1],liA[i+heng],liB[i+1],liB[i+heng],liC[i+1],liC[i+heng]:
        if maxValue==j:
            emptyLi.append(j)
    if len(emptyLi)!=1:
        emptyLi=[]
        i=i+5
        #print(i,"nowLocation")
    else:
        emptyLi=[]
        #print(liA[i+1],liB[i+1],liC[i+1],maxValue)
        if int(liA[i+1])==int(maxValue):
            i=i+1
            #print(i,"nowLocation1")
        if int(liB[i+1])==int(maxValue):
            i=i+1
            #print(i,"nowLocation11")
        if int(liC[i+1])==int(maxValue):
            i=i+1
            #print(i,"nowLocation111")
        if liA[i+heng]==maxValue:
            i=i+heng
            #print(i,"nowLocation2")
        if liB[i+heng] ==maxValue:
            i=i+heng
            #print(i,"nowLocation2")
        if liC[i+heng]==maxValue:
            i=i+heng
            #print(i,"nowLocation2")
    """if i>=shu*heng-heng:
        break"""

""" try:
    i=liA.index(maxValue)
except Exception:
    pass

try:
    i=liB.index(maxValue)
except Exception:
    pass

try:
    i=liC.index(maxValue)
except Exception:
    pass"""
print(minValue)
