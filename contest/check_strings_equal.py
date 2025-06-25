# https://leetcode.com/contest/weekly-contest-438/problems/check-if-digits-are-equal-in-string-after-operations-i/
# Incomplete 

from math import ceil 

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s_digits = [int(val) for val in s]
        n = len(s_digits)
        val0 = s_digits[0]
        val1 = s_digits[1]

        sm0 = val0
        prevsm1 = val1
        sm1 = val1 
        for ind in range(1, n-1): 
            # print('sm0', sm0, s_digits[ind], val0)
            sm0 = (sm0 + sm1)%10
            ind1 = ind + 1
            newsm1_p1 = sm1
            newsm1_p2 = (sm1 - prevsm1) if ind1 > 2 else 0
            half_ind = s_digits[1] if ind1 > 2 else s_digits[0]
            newsm1_half = s_digits[half_ind]
            newsm1_p3_p1 = newsm1_p2 - newsm1_half if ind1 > 2 else 0
            newsm1_p3 = newsm1_p3_p1 + s_digits[ind+1]
            newsm1 = (newsm1_p1 + newsm1_p2 + newsm1_p3)%10
            print(newsm1_p1, newsm1_p2, newsm1_p3, newsm1_half,  s_digits[ind+1])
            print('sm1', prevsm1, sm1, newsm1, newsm1_p1, newsm1_p2, newsm1_p3, s_digits[ind+1])
            print(newsm1)
            prevsm1 = sm1 
            sm1 = newsm1


        print([sm0, sm1])
        return sm0 == sm1

    def hasSameDigits2(self, s: str) -> bool:
        s_digits = [int(val) for val in s]
        append_lst = list(s)
        while(len(s_digits) > 2): 
            new_s_digts = []
            new_append_lst = []
            for ind in range(len(s_digits) - 1):
                new_val = (s_digits[ind] + s_digits[ind+1])%10
                new_s_digts.append(new_val) 
                new_val = append_lst[ind] + append_lst[ind+1]
                new_append_lst.append(new_val)
            s_digits = new_s_digts
            append_lst = new_append_lst
            print(append_lst)
        
       
        hsh = {}
        for s in append_lst[0]:
            hsh[s] = hsh.get(s, 0) + 1
        # print(hsh.keys())
        # print(hsh.values())
        print(s_digits)
        return s_digits[0] == s_digits[1]
    
sol = Solution()
s = "123456"
sol.hasSameDigits(s)
sol.hasSameDigits2(s)