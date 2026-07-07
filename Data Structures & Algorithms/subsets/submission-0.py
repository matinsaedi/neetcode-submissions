# Bit Manipulation Version

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []

        for mask in range(2 ** n):
            s = []
            for i in range(n):
                if mask & (1 << i):
                    s.append(nums[i])
            subsets.append(s)

        return subsets