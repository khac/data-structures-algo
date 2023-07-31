# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_index = []
        product_nums = 1
        for i,num in enumerate(nums):
            if num != 0:
                product_nums = product_nums * num
            else:
                zero_index.append(i)
        if len(zero_index) > 1:
            return [0]*len(nums)
        elif len(zero_index) == 1:
            retArr = [0]*len(nums)
            retArr[zero_index[0]] = product_nums
            return retArr
        return [product_nums//num for num in nums]
