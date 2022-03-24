# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapping = dict()
        for ind,val in enumerate(nums):
            mapping[val] = ind
            
        for i in nums:
            y = target - i
            
            if y == i :
                if len(set(nums)) == len(nums):
                    continue
                else:
                    return [ind for ind,x in enumerate(nums) if x == y ]
                
            
            if y in mapping.keys():
                
                return [mapping[i],mapping[y]]
            
        return 0