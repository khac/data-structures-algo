# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArraySum, curSubArraySum = -inf, -inf

        for num in nums:
            curSubArraySum = max(curSubArraySum+num, num)
            maxSubArraySum = max(maxSubArraySum, curSubArraySum)
        return maxSubArraySum

"""
TC - O(N)
SC - O(1)

Follow up - return the maximum subarray

nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArraySumCumulative = [-2,1,-2,4, 3,5,6,1,5]

returnArr = []
traverse backward from end till we find the maxSubArraySum
returnArr = [1,]
keep traversing backward till nums[i] == maxSubArraySumCumulative[i]
returnArr = [1,2,-1,4]
break

return reversed(returnArr)
[4,-1,2,1]
"""
