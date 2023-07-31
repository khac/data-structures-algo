# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.chars:
                node.chars[char] = TrieNode()
            node = node.chars[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        def dfs(node, word, index):
            if index == len(word):
                return node.isWord
            if word[index] != '.':
                if word[index] in node.chars:
                    return dfs(node.chars[word[index]], word, index+1)
                else:
                    return False
            return any(dfs(node.chars[next_node], word, index+1) for next_node in node.chars)

        return dfs(node, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
