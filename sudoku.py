def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    res=[]
    path=[]
    import copy
    def backtracking(board):
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    continue
                for x in range(1,10):
                    if isValid(i,j,str(x))==True:
                        board[i][j]=str(x)
                        if backtracking(board) ==True:
                            return True
                        board[i][j]="."
                return False
        return True
    def isValid(di,dj,dx):
        if dx in board[di]:
            return False
        for i in range(9):
            if dx == board[i][dj]:
                return False
        row=di//3*3
        col=dj//3*3
        for i in range(3):
            for j in range(3):
                if board[row+i][col+j]==dx:
                    return False
        return True
    backtracking(board)
    return board