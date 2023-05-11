def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res=[]
    path=[]
    def backtrack(n,k,startIndex):
        if len(path) == k:
            res.append(path[:])
            print(path,res)
            return 
        for i in range(startIndex,n-(k-len(path))+2):
            path.append(i)
            print(path)
            backtrack(n,k,i+1)
            path.pop()
    backtrack(n,k,1)
    return res

combine(4,2)