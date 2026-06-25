class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        max_left, max_right = 0, 0
        water = 0

        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                water += max_left - height[l]
                l += 1
                
            else:
                max_right = max(max_right, height[r])
                water += max_right - height[r]
                r -= 1
                
        return water
        