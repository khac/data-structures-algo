
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        """
        cbaaaabc
        
        c max_len = 1 
        cb max_len = 1 l = 1
        cba max_len = 2, l = 1, r = 2, r-l+1 
        cbaa max_len = 3, l = 1, r = 3, r-l+1 
        cbaaa max_len = 3, l = 3, r = 4, r-l+1 
        cbaaab max_len = 3, l = 3, r = 5, r-l+1 
        cbaaaabc max_len = 4, l = 3, r = 6, r-l+1 
        
        
        "aaaab aaacc"
        ["bcca","aaa","aabaa","baaac"]
        
        
        time complexity: O(n*(10+10))
        space complexity : O(1)
        
        """
        max_len = 0
        l = 0
        n = len(word)
        forbidden = set(forbidden)
        for r in range(n):
            for index in range(r, max(r-10, l-1), -1):
                cur_word = word[index:r+1]
                if cur_word in forbidden:
                    l = index+1
                    break
            if r-l+1>max_len:
                max_len = max(max_len, r-l+1)
        return max_len
