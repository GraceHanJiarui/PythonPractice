def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    minute=0
    queue=[]
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==2:
                queue.append([i,j])
            elif grid[i][j]==1:
                count+=1
    if count==0:
        return 0
    if queue==[] and count!=0:
        return -1
    
    while queue:
        for i in range(len(queue)):
            i,j=queue.pop(0)
            for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                nexti,nextj=i+di,j+dj
                if nexti>=0 and nextj>=0 and nexti<len(grid) and nextj<len(grid[0]) and grid[nexti][nextj]==1:
                    grid[nexti][nextj]=2
                    queue.append([nexti,nextj])
                    count-=1
        print(queue)
        minute+=1

    if count!=0:
        return -1
    else:
        return minute-1