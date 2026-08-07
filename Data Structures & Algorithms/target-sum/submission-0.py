class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, current_sum):
            if i >= len(nums):
                return 1 if current_sum == target else 0

            if (i, current_sum) in dp:
                return dp[(i, current_sum)]

            result = (dfs(i + 1, current_sum + nums[i]) +
                      dfs(i + 1, current_sum - nums[i]))

            dp[(i, current_sum)] = result 
            return result

        dfs(0, 0)
        return dp[(0, 0)]


            
            
        