# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        
        pair = {"(":")","[":"]","{":"}"}
        
        
        for ele in s:
            if ele in pair:
                stack.append(ele)
            else:
                if not stack:
                    return False
                else:
                    conj = stack.pop()
                
                
                if ele != pair[conj]:
                    return False
                
        if not stack:
            return True
        else:
            return False
