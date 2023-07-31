# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        rightmost = nums[-1]
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid] > rightmost:
                l = mid+1
            else:
                r = mid-1
        return 0
