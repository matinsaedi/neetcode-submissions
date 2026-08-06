class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[1] * (len(coins) + 1)] + [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        coins.sort()
        
        for i in range(1, amount + 1):
            for j in range(len(coins) - 1, -1, -1):
                if i < coins[j]:
                    continue
                
                dp[i][j] = dp[i][j + 1] + dp[i - coins[j]][j]

        return dp[amount][0]



