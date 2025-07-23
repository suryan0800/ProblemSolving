# https://leetcode.com/problems/powx-n/?envType=study-plan-v2&envId=top-interview-150 

class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {}
        if n < 0: 
            x = 1/x
            n = -n
        return self.recursive_solve(x, n, dp)

    def recursive_solve(self, x, n, dp): 
        if n == 1: return x 
        if n == 0: return 1 
        if n in dp: return dp[n]
        n1 = int(n/2)
        n2 = n - n1
        new_val = self.recursive_solve(x, n1, dp) * self.recursive_solve(x, n2, dp)
        dp[n] = new_val
        return new_val 
        
sol = Solution() 
sol.myPow(2.000, -2)