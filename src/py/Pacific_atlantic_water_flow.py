# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        pacific, atlantic = [[False]*n for _ in range(m)],[[False]*n for _ in range(m)]

        def dfs(row, col, memo):
            memo[row][col] = True
            for nrow, ncol in [[row+1, col],[row-1, col],[row, col+1],[row, col-1]]:
                if 0<=nrow<m and 0<=ncol<n and not memo[nrow][ncol] and heights[nrow][ncol] >= heights[row][col]:
                    dfs(nrow, ncol, memo)

        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-1,atlantic)
        for i in range(n):
            dfs(0,i,pacific)
            dfs(m-1,i,atlantic)

        result = []
        for i,j in product(range(m), range(n)):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i,j])
        return result
