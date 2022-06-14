class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid = [[0]*(n+2)] + [[0]+grid[i]+[0] for i in range(m)] + [[0]*(n+2)]
        dx=0,0,1,-1
        dy=1,-1,0,0
        def dfs(x,y):
            grid[x][y] = 0
            cnt = 1
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if grid[nx][ny]:
                    cnt += dfs(nx,ny)
            return cnt
        
        mCnt=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if grid[i][j]:
                    mCnt = max(mCnt, dfs(i,j))
        return mCnt