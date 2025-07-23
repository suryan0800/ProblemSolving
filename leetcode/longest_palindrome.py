# https://leetcode.com/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_size = len(s)
        arr = [[False for _ in range(s_size)] for _ in range(s_size)]

        for ind in range(s_size): 
            arr[ind][ind] = True 

        mx_ind1, mx_ind2 = 0, 0
        for ind in range(s_size - 1): 
            if s[ind] == s[ind+1]: 
                arr[ind][ind+1] = True 
                mx_ind1, mx_ind2 = ind, ind + 1
        

        for pal_size in range(2, s_size): 
            for ind1 in range(s_size - pal_size): 
                ind2 = ind1 + pal_size
                if s[ind1] == s[ind2] and arr[ind1+1][ind2-1]:
                    arr[ind1][ind2] = True 
                    mx_ind1, mx_ind2 = ind1, ind2

        return s[mx_ind1: mx_ind2+1]



        
sol = Solution()
sol.longestPalindrome('aacabdkacaa')