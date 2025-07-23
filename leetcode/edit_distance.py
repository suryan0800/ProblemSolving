# https://leetcode.com/problems/edit-distance/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        arr = [[0] * (m+1) for _ in range(n+1)]

        for ind in range(1, n+1): 
            arr[ind][0] = arr[ind-1][0] + 1

        for ind in range(1, m+1): 
            arr[0][ind] = arr[0][ind-1] + 1 

        for ind1 in range(1, n+1): 
            for ind2 in range(1, m+1): 
                ch1 = word1[ind1-1]
                ch2 = word2[ind2-1] 
                ins_case = arr[ind1][ind2-1] + 1 
                del_case = arr[ind1-1][ind2] + 1
                rep_case = arr[ind1-1][ind2-1] + (1 if ch1 != ch2 else 0)
                arr[ind1][ind2] = min(ins_case, del_case, rep_case)

        # print(word2)
        # for ind in range(n+1): 
        #     print(arr[ind])
        return arr[n][m]

sol = Solution()
sol.minDistance('dao', 'ros')