def solveNQueens(self, n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    res=[]
    mat=[["." for i in range(n)] for j in range(n)]
    def backtrack(i):
        if i==n:
            path=[]
            print(mat)
            for i in mat:
                temp="".join(i)
                path.append(temp)
            res.append(path[:])
            return 
        for j in range(n):
            if isValid(i,j,mat)==True:
                mat[i][j]="Q"
                backtrack(i+1)
                mat[i][j]="."
        return
    
    def isValid(i,j,mat):
        for x in range(0,i):
            if mat[x][j]=="Q":
                return False
            if i-x-1>=0 and j+x+1<n:
                if mat[i-x-1][j+x+1]=="Q":
                    return False
            if i-x-1>=0 and j-x-1>=0:
                if mat[i-x-1][j-x-1]=="Q":
                    return False
        return True

    backtrack(0)
    return res