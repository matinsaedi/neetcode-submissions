class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        subsets = []
        s = []

        def dfs(i):
            if i >= len(nums):
                subsets.append(s.copy())
                return

            s.append(nums[i])
            dfs(i + 1)

            s.pop()

            while (i < len(nums) - 1) and (nums[i + 1] == nums[i]):
                i += 1
            dfs(i + 1)
        
        dfs(0)
        return subsets