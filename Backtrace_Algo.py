input1=input().split(",")

def judge(input1):
    j=0
    for i in input1:
        if int(i)+j!=:
            j=i
        elif i==j:
            return False
    return True

def dfs(input1):
    result=[]
    def backtrack(input1, track):

        if 
            result.append(track[:])
            print(result,"result")
            return

        for i in range(len(input1)):
            if i>0 and (input1[i]==input1[i-1]):#循环中不符合要求的pass掉
                continue
            print([input1[i]],"track",track)
            backtrack(input1[:i]+input1[i+1:],track+[input1[i]])
    backtrack(input1,[])
    return result
print(dfs(input1))
