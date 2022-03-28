# https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        nums = sorted(nums)
        
        a = nums[-1]
        b = nums[-2]
        c = nums[-3]
        
        def check_tri(a,b,c):
            
            if b+c > a :
                if a+b > c:
                    if a+c > b:
                        return True
                    else:
                        return False
                else:
                    return False                    
            else:
                return False
            
        if check_tri(a,b,c) is False :
            
            if len(nums) >3:                        
                
                for i in range(len(nums)-2,1,-1):
                    a = nums[i]
                    b = nums[i-1]
                    c = nums[i-2]
                    
                    if check_tri(a,b,c):
                        return sum([a,b,c])
                
                return 0
                        
                    
            else:
                return 0
            
        else:
            return sum([a,b,c])
        