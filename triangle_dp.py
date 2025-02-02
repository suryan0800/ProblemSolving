# https://leetcode.com/problems/triangle/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        triangle_len = len(triangle)
        for ind in range(triangle_len-1): 
            ind2 = triangle_len - ind - 1 
            for ind3 in range(1, len(triangle[ind2])): 
                val = min(triangle[ind2][ind3], triangle[ind2][ind3-1])
                triangle[ind2-1][ind3-1] = triangle[ind2-1][ind3-1] + val 

        return triangle[0][0]

sol = Solution() 
sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

