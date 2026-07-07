# Backtracking Version

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subsets = []
        s = []

        def dfs(i):
            if i >= n:
                subsets.append(s.copy())
                return

            s.append(nums[i])
            dfs(i + 1)
            s.pop()
            dfs(i + 1)

        dfs(0)
        return subsets