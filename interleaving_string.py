# https://leetcode.com/problems/interleaving-string/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        n = len(s1)
        m = len(s2) 
        if (n + m) != len(s3): return False 

        arr = [[False] * (m + 1) for _ in range(n+1)]
        arr[0][0] = True 
        for ind in range(1, n + 1): 
            arr[ind][0] = arr[ind-1][0] and s1[ind-1] == s3[ind-1]

        for ind in range(1, m + 1): 
            arr[0][ind] = arr[0][ind-1] and s2[ind-1] == s3[ind-1]

        for ind1 in range(1, n+1): 
            for ind2 in range(1,m+1):
                # print(s1[ind1-1], s2[ind2-1], s3[ind1+ind2-1])
                arr[ind1][ind2] = ((s1[ind1 - 1] == s3[ind1+ind2-1]) and arr[ind1-1][ind2]) or ((s2[ind2 - 1] == s3[ind1+ind2-1]) and arr[ind1][ind2-1])

        # print(s2)
        # for ind in range(n+1): 
        #     print(arr[ind])
        return arr[n][m]
        
        
sol = Solution()
sol.isInterleave("a", "", "a")