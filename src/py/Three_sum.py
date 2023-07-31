# 15. 3Sum
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        """
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]

        [-2,0,0,2,2]
        
        """
        returnArr = []
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums)-1
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    returnArr.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while r>l and nums[r] == nums[r+1]:
                        r -= 1
                    # while l<r and nums[l] == nums[l-1]:
                    #     l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return returnArr
