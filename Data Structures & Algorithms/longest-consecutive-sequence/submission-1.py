class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if (num - 1) in nums_set:
                continue
            
            length = 0
            current = num
            
            while current in nums_set:
                length += 1
                current += 1

            max_length = max(max_length, length)

        return max_length