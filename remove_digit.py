# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/ 

class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """

        cnt = 0
        for ch in number: 
            if ch == digit: 
                cnt += 1
        result = ''
        for ind, ch in enumerate(number): 
            if ch == digit: 
                print(ch, number[ind], cnt)
                if cnt == 1: 
                    ind += 1
                    break 
                if ch >= number[ind+1]: 
                    result += ch 
                else: 
                    ind += 1
                    break
                cnt -= 1
            else: 
                result += ch
        for ind2 in range(ind, len(number)):
            result += number[ind2]

        return result 
    
sol = Solution()
sol.removeDigit('1231', '1')