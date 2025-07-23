# https://leetcode.com/problems/palindrome-number/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        y = 0
        pw = 1
        tp = x
        while tp > 0: 
            digit = tp%10
            y = y * 10 + digit 
            pw *= 10
            tp /= 10
            tp = int(tp)
            # print(digit, tp)
        # print (x, y)
        # print(lst)
        return x == y 

sol = Solution()
sol.isPalindrome(12121)