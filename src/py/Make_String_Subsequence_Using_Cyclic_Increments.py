class Solution:
    
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        index = 0
        
        def isMatch(char1, char2):
            
            if char1 == char2 or \
                (ord(char1)-ord('a')+1)%26 == ord(char2)-ord('a'):
                return True
            return False
        
        for char in str1:
            if isMatch(char, str2[index]):
                index += 1
                # print(char, str2[index])
            if index == len(str2):
                break
        return index == len(str2)
