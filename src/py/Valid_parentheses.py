# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', '}':'{', ']':'['}
        open_brackets = map.values()
        stack = []
        for bracket in s:
            if bracket in open_brackets:
                stack.append(bracket)
            else:
                if not stack: return False
                if map[bracket] != stack[-1]:
                    return False 
                else:
                    stack.pop()
        return len(stack) == 0
