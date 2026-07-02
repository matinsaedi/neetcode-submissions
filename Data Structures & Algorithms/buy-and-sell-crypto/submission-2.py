class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        output = 0
        min_prev = prices[0]

        for p in prices:
            profit = p - min_prev
            output = max(output, profit)

            min_prev = min(min_prev, p)
        
        return output