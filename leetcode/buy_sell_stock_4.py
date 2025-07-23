# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/?envType=study-plan-v2&envId=top-interview-150
# Tutorial: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/solutions/6225207/beats-100-solution-2-approaches-8-solutions-recursion-memo-tabulation-space-optimization/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        # dp[index, buy/sell, cnt]
        n = len(prices)
        dp = [[0 for _ in range(k+1)] for _ in range(2)]

        for ind1 in range(n-1, -1, -1): 
            for ind2 in range(2): 
                for ind3 in range(1, k+1):
                    if ind2: # Buy phase previous time
                        buy_profit =  (-prices[ind1] + dp[0][ind3]) 
                        nobuy_profit = 0 + dp[1][ind3]
                        profit = max(buy_profit, nobuy_profit)
                    else: 
                        sell_profit = prices[ind1] + dp[1][ind3-1]
                        nosell_profit = 0 + dp[0][ind3]
                        profit = max(sell_profit, nosell_profit) 
                    dp[ind2][ind3] = profit 

        # print(dp)
        return dp[1][k]
        

sol = Solution()
sol.maxProfit(2, [3,2,6,5,0,3])