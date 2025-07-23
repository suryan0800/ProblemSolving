# https://leetcode.com/problems/sqrtx/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def mySqrt(self, x: int) -> int:
        mnval = 0
        mxval = x
        sqval = x * x
        midval = x
        while (mxval - mnval) > 1:
            midval = mnval + int((mxval - mnval)/2) 
            sqval = midval * midval
            if sqval > x: 
                mxval = midval 
            elif sqval < x: 
                mnval = midval 
            else: 
                return midval
        # print(midval, sqval)
        if sqval > x: return midval - 1
        return  midval
    
sol = Solution()
sol.mySqrt(1)