# https://leetcode.com/problems/coin-change/description/
# Tutorial: https://leetcode.com/problems/coin-change/solutions/6162873/video-keep-minimum-number-of-coins-to-make-up-each-amount/

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        amounts = [(amount + 1)] * (amount + 1) 
        amounts[0] = 0
        
        for ind in range(1, amount+1):
            min_cnt = amounts[ind]
            curr_amount = ind 
            for coin in coins: 
                rem = curr_amount - coin 
                if rem >= 0: 
                    cnt = amounts[rem] + 1 
                    min_cnt = min(min_cnt, cnt)
            amounts[ind] = min_cnt 
            
        return amounts[amount]  if amounts[amount] <= amount else -1

sol = Solution()
sol.coinChange([186, 419, 83, 408], 6249)
# sol.coinChange([1, 2, 5], 11)
# sol.coinChange([3,7,405,436], 8839)
# sol.coinChange([418,419,420,421,422], 9864)
