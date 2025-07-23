# https://leetcode.com/problems/unique-paths-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        row_size = len(obstacleGrid)     
        col_size = len(obstacleGrid[0])     
        paths_count = [[0 for _ in range(col_size)] for _ in range(row_size)] 
        paths_count[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        for ind in range(1, row_size): 
            paths_count[ind][0] = 0 if obstacleGrid[ind][0] == 1 else paths_count[ind-1][0]

        for ind in range(1, col_size): 
            paths_count[0][ind] = 0 if obstacleGrid[0][ind] == 1 else paths_count[0][ind-1]

        for ind1 in range(1, row_size): 
            for ind2 in range(1, col_size): 
                imm_top = ind1 -1 
                imm_left = ind2 - 1
                val1 = paths_count[imm_top][ind2]
                val2 = paths_count[ind1][imm_left] 
                # print(paths_count, obstacleGrid)
                paths_count[ind1][ind2] = 0 if obstacleGrid[ind1][ind2] == 1 else sum([val1, val2])

        # print(paths_count)
        return paths_count[row_size - 1][col_size - 1]


sol = Solution()
sol.uniquePathsWithObstacles([[0,0],[1,0]])