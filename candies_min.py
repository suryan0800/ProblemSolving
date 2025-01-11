# https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150 

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        candies = [1] * len(ratings) # 'U' - uptrend, 'D' - downtrend, 'N' - Neutral trend
        for ind in range(1, len(ratings)): 
            diff = ratings[ind] - ratings[ind-1]
            if diff > 0: 
                candies[ind] = candies[ind-1] + 1
        
        for ind in range(len(ratings)-2, -1, -1):
            diff = ratings[ind] - ratings[ind+1]
            if diff > 0: 
                candies[ind] = max(candies[ind+1] + 1, candies[ind])
        print(candies)
        return sum(candies)
    
sol = Solution()
sol.candy([1,3,4,5,2])