# https://leetcode.com/problems/two-sum/ 

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hsh = {}
        for ind, num in enumerate(nums): 
            print(ind, num, nums_hsh.get(num, []).append(ind))
            nums_hsh[num] = nums_hsh.get(num, []).append(ind)
        print(nums_hsh)
        for num1 in nums_hsh: 
            num2 = target - num1 
            if num2 in nums_hsh: 
                if num1 != num2:
                    return [nums_hsh[num1][0], nums_hsh[num2][0]]
                elif len(nums_hsh[num2]) >= 2: 
                    return [nums_hsh[num1][0], nums_hsh[num2][1]]
        
        return [None, None]
            
sol = Solution()
sol.twoSum([2,7,11,15], 9)
