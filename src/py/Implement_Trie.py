class TrieNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # print(char)
            if char not in node.chars:
                node.chars[char] = TrieNode()
            node = node.chars[char]
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # print(char)
            if char not in node.chars:
                return False
            node = node.chars[char]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.chars:
                return False
            node = node.chars[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
