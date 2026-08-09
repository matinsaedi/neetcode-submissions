class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = nums[0]
        maxSum = nums[0]

        for num in nums[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum
                
        # dp = [0] * len(nums)
        # dp[0] = nums[0]

        # for i in range(1, len(nums)):
        #     if dp[i - 1] < 0:
        #         dp[i] = nums[i]
            
        #     else:
        #         dp[i] = dp[i - 1] + nums[i]