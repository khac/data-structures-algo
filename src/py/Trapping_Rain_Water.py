# 42. Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        water_trap = 0
        l,r = 0, len(height)-1
        max_l, max_r = height[0], height[-1]
        while l<r:
            if height[l]<height[r]:
                water_trap += max(0, min(max_l, max_r) - height[l])
                l += 1
                max_l = max(max_l, height[l])
            else:
                water_trap += max(0, min(max_l, max_r) - height[r])
                r -= 1
                max_r = max(max_r, height[r])
        return water_trap
