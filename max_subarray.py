# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_global = nums[0]
        max_local = nums[0]
        
        for i in nums[1:]:
            max_local = max(i,max_local+i)
            max_global = max(max_local,max_global)
            
        return max_global