# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        import math
        power_c = 1
        
        arr = []
        
        while n > 0:
            
            arr.append(n% 10)
            n = n//10
            
        prod = math.prod(arr)
        sum_ar = sum(arr)
        
        return prod-sum_ar
            
            