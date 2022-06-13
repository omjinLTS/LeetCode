class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        grid = [['0']*(n+2)] + [['0']+grid[i]+['0'] for i in range(m)] + [['0']*(n+2)]
        dx=0,0,1,-1
        dy=1,-1,0,0
        def dfs(x,y):
            grid[x][y] = '0'
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if grid[nx][ny]=='1':
                    dfs(nx,ny)
        cnt=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if grid[i][j]=='1':
                    dfs(i,j)
                    cnt+=1
        return cnt