"""
853. Car Fleet
https://leetcode.com/problems/car-fleet/

TC - O(n)
SC - O(n)
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        [1, 7, 12]
        """
        stack = []
        n = len(position)
        pos_speed = [(p,s) for (p,s) in zip(position, speed)]
        pos_speed.sort(reverse=True)

        for i in range(n):
            time = (target-pos_speed[i][0])/pos_speed[i][1]
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)
