# https://leetcode.com/problems/richest-customer-wealth


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        return max([sum(we) for we in accounts])
