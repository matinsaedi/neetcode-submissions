class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        x1 = 0
        for i in range(0, len(nums) + 1):
            x1 ^= i

        x2 = 0
        for num in nums:
            x2 ^= num

        return x1 ^ x2