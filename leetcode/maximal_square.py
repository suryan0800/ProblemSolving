# https://leetcode.com/problems/maximal-square/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[0] * (m+1) for _ in range(n+1)]

        mx_square_with_1 = 0
       
        for end_ind1 in range(n):
            for end_ind2 in range(m):
                if matrix[end_ind1][end_ind2] == "1": 
                    square_size = min(dp[end_ind1-1][end_ind2-1], dp[end_ind1-1][end_ind2], dp[end_ind1][end_ind2-1]) + 1
                    dp[end_ind1][end_ind2] = square_size 
                    if mx_square_with_1 < square_size: 
                        mx_square_with_1 = square_size

        return mx_square_with_1 * mx_square_with_1



sol = Solution() 
sol.maximalSquare([
    ["1","1","1","1","1","1","1","1"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","1","1","0"],
    ["1","1","1","1","1","0","0","0"],
    ["0","1","1","1","1","0","0","0"]])