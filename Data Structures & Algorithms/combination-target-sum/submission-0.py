class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        combinations = []
        c = []
        
        def dfs(i, total):

            if total == target:
                combinations.append(c.copy())
                return

            if i >= len(nums) or total > target:
                return

            c.append(nums[i])
            dfs(i, total + nums[i])
            c.pop()
            dfs(i + 1, total)

        dfs(0, 0)
        return combinations

