# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        d = arr[1]-arr[0]
        
        if len(arr) > 2:
            
            for i in range(2,len(arr)):
                
                if arr[i]-arr[i-1] == d:
                    continue
                else:
                    return False
                
            return True
        else:
            return True