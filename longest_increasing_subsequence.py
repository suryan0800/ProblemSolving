# https://leetcode.com/problems/longest-increasing-subsequence/?envType=study-plan-v2&envId=top-interview-150 
# Tutorial: https://leetcode.com/problems/longest-increasing-subsequence/solutions/74848/9-lines-c-code-with-o-nlogn-complexity/?envType=study-plan-v2&envId=top-interview-150 

from bisect import bisect_left 

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = []
        for val in nums: 
            ind = bisect_left(res, val) 
            if ind == len(res): 
                res.append(val)
            else:  
                res[ind] = val

        # print(res)
        return len(res)
        


        
sol = Solution() 
sol.lengthOfLIS([10,9,2,5,3,7,101,18])