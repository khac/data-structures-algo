# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        right_most = nums[-1]
        while left<=right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            elif target > right_most:
                if nums[mid] <= right_most or nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if nums[mid] > right_most or nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
