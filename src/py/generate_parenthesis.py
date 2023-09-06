"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

"", 0, 0

"(" 1 0
"((" 2 0
"(((" 3 0
"((()" 3 1
"((())" 3 2
"((()))" 3 3
"(()" 2 1
"()" 2 1
TC - O(2**(2n)) - O(4**n)
SC - O(2**(2n)) - O(4**n)

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        paren = []
        def recursion(arr, open, close):
            if open == n and close == n:
                paren.append(''.join(list(arr)))
                return
            if open>=close and open<n:
                arr.append('(')
                recursion(arr, open+1, close)
                arr.pop()
            if close<open:
                arr.append(')')
                recursion(arr, open, close+1)
                arr.pop()
            
        recursion([],0,0)
        return paren
