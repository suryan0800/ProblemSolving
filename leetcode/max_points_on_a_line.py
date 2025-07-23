# https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150 

from math import sqrt

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        return self.point_falls_on_a_line(*points)
    
    def point_falls_on_a_line(self, p1, p2, p3): 
        return ((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]) == 0)


sol = Solution()
sol.maxPoints([[1,1],[2,2],[5,5]])