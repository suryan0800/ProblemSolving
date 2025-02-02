# https://leetcode.com/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-interview-150 

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        row_size = len(grid)     
        col_size = len(grid[0])      
        for ind in range(1, row_size): 
            grid[ind][0] += grid[ind - 1][0]

        for ind in range(1, col_size): 
            grid[0][ind] += grid[0][ind - 1]

        for ind1 in range(1, row_size): 
            for ind2 in range(1, col_size): 
                imm_top = ind1 -1 
                imm_left = ind2 - 1
                val1 = grid[imm_top][ind2]
                val2 = grid[ind1][imm_left] 
                grid[ind1][ind2] += min(val1, val2)

        # print(grid)
        return grid[row_size - 1][col_size - 1]
    
sol = Solution()
sol.minPathSum([[1,2,3],[4,5,6]])
        