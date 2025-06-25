# https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[[None for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(n+1)]
        val = self.recursive_solve(0, 0, k, limits[0], grid, limits, dp)
        for i in range(n):
            for j in range(m):
                print(dp[i][j])
        return val

    def recursive_solve(self, i, j, curr_k, row_limit, grid, limits, dp): 
        if (i > len(grid) or (j > len(grid[0])) or curr_k <= 0):
            return 0
        
        # print(i, j, curr_k, row_limit)
        if dp[i][j][curr_k] is not None: 
            return dp[i][j][curr_k]
        
        if ((j+1) < len(grid[0])) and row_limit > 0: 
            newi = i 
            newj = j + 1
            newrow_limit = row_limit
        else: 
            newi = i + 1
            newj = 0
            newrow_limit = limits[newi] if newi < len(grid) else 0
        # print(i,j)
        if row_limit <= 0: 
            val1 = 0
        else: 
            val1_newrow_limit = newrow_limit - 1 if newi == i else newrow_limit 
            val1 = grid[i][j] + self.recursive_solve(newi, newj, curr_k-1, val1_newrow_limit, grid, limits, dp)
        val2 = 0 + self.recursive_solve(newi, newj, curr_k, newrow_limit, grid, limits, dp) 

        max_val = max(val1, val2)
        dp[i][j][curr_k] = max_val 

        # if val1 > val2: 
        #     print(i, j, grid[i][j], max_val, curr_k, row_limit)
        return max_val 
        

sol = Solution()
# sol.maxSum([[1,2],[3,4]], [1,2], 2)
# sol.maxSum([[5,3,7],[8,2,6]], [2,2], 3)
# sol.maxSum([[5,8,6,1,6,4]], [3], 3)
# sol.maxSum([[7,10,3,3,7,7,0],
#             [5,5,9,2,10,5,2]], [3,7], 7)
sol.maxSum([[16,18,7,27,43,45,50,4,29],
            [31,8,42,26,47,47,23,22,40]], [8,2], 6)