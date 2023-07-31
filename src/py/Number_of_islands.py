# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count,m,n = 0,len(grid), len(grid[0])

        def dfs(x,y):
            if 0<=x<m and 0<=y<n and grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x-1,y)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x,y+1)

        for i,j in product(range(m), range(n)):
            if grid[i][j] == "1":
                dfs(i,j)
                count += 1
        return count
