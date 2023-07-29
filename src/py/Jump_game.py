# 55. Jump Game
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump_limit = 0
        for i in range(len(nums)):
            if max_jump_limit < i:
                return False
            if max_jump_limit >= len(nums)-1:
                break
            max_jump_limit = max(max_jump_limit, i+nums[i])
        return True
