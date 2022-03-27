# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low % 2 != 0 or high %2 != 0 : # low is odd
            
            return (high -low)//2 +1
        else:
            return (high -low)//2