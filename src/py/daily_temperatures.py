"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Monotonic increasing stack
TC - O(n)
SC - O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
            [73,74,75,71,69,72,76,73]
            [1]
            [1]

        """
        n = len(temperatures)
        retArr = [0]*n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                retArr[index] = i-index
            stack.append(i)
        return retArr
