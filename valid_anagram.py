# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        
        from collections import Counter 
        
        s_c = dict(Counter(s))
        t_c = dict(Counter(t))
        
        for i in s:
            if i in s_c and i in t_c:
                if s_c[i] == t_c[i]:                    
                    continue
                return False            
            else:
                return False
            
        return True