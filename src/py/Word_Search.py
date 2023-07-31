# 79. Word Search
# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def dfs(index, x, y):
            if index == len(word):
                return True
            
            if 0<=x<m and 0<=y<n and board[x][y] == word[index]:
                temp = board[x][y]
                board[x][y] = '#'
                for nx, ny in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    if dfs(index+1, nx, ny):
                        return True
                board[x][y] = temp
            return False
        
        for i,j in product(range(m), range(n)):
            if dfs(0,i,j):
                return True
        return False
