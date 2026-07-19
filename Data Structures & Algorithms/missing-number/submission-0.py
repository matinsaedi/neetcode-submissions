class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s = set(nums)

        for num in range(0, len(nums) + 1):
            if num not in s:
                return num