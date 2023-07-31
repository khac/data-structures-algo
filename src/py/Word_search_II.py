# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.chars:
                node.chars[char] = TrieNode()
            node = node.chars[char]
        node.isWord = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        
        def dfs(i,j, node, result):
            if node.isWord:
                node.isWord = False
                result.append(node.word)

            if 0<=i<m and 0<=j<n and board[i][j] in node.chars:
                temp = board[i][j]
                board[i][j] = '#'
                for (x,y) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    dfs(x,y, node.chars[temp], result)

                board[i][j] = temp

        
        
        m,n,result = len(board), len(board[0]), []
        for i,j in product(range(m), range(n)):
            dfs(i, j, trie.root, result)

        return result
