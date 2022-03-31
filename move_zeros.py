# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        p_pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p_pos] = nums[i]
                p_pos +=1
        
        for i in range(p_pos,len(nums)):
            nums[i] = 0
