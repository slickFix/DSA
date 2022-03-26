# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        pro = 0
        buy_p = prices[0]
        
        
        for ele in prices[1:]:
            
            if ele < buy_p:
                
                buy_p = ele
                
            pro = max(pro, ele - buy_p)
            
        return pro