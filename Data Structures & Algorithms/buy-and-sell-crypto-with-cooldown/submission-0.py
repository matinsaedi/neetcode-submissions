class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = - prices[i] + dfs(i + 1, False)
                cooldown = dfs(i + 1, True)
                result = max(buy, cooldown)
                
            else:
                sell = prices[i] + dfs(i + 2, True)
                cooldown = dfs(i + 1, False)
                result = max(sell, cooldown)

            dp[(i, buying)] = result
            return result

        return dfs(0, True)
            



        