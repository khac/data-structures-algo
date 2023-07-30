# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        returnArr = []
        candidatesArr = []

        def dfs(index, sum):
            if sum == target:
                returnArr.append(list(candidatesArr))
                return
            
            for i in range(index, len(candidates)):
                if candidates[i] + sum > target:
                    return
                candidatesArr.append(candidates[i])
                dfs(i, sum+candidates[i])
                candidatesArr.pop()
        dfs(0, 0)
        return returnArr
