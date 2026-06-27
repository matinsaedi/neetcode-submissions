class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        max_left, max_right = 0, 0
        water = 0
        while l <= r:
            if max_left < max_right:
                s = max_left - height[l]
                max_left = max(max_left, height[l])
                
                if s > 0:
                    water += s

                l += 1

            else:
                s = max_right - height[r]
                max_right = max(max_right, height[r])

                if s > 0:
                    water += s

                r -= 1
                
        return water



        