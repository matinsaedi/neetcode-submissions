class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        current_max = nums[0]
        current_min = nums[0]
        res = nums[0]

        for i in nums[1:]:
            candidates = [i, i * current_max, i * current_min]
            current_max = max(candidates)
            current_min = min(candidates)
            res = max(res, current_max)

        return res