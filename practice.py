import itertools
inputInit=input().split(",")
input0=inputInit[0]
input1=inputInit[1]
res=[]
"""li=[i for i in itertools.permutations(input0,len(input0))]
print(j)"""
for j in itertools.permutations(input0,len(input0)):
    if j[0]=="0":
        j=j[1:]
        print(j,"j")
    res.append(j)
print(j)
print(sorted(res)[0])
print(sorted(res)[0],sorted(res,reverse=True)[0],sorted(res,reverse=True)[49],sorted(res)[int(input1)-1])
