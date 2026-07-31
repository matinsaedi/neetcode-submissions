class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1

        for i in range(n - 2, -1, -1):
            candidates = [1]
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    candidates.append(1 + dp[j])

            dp[i] = max(candidates)
            res = max(res, dp[i])

        return res



        # for i in (5, 4, 3, 2, 1, 0):
        #     for j in (6, 7):
        #         3 < 7:
        #         candidates = [1, 1 + 1]



