# https://leetcode.com/problems/ransom-note/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        mg = dict(Counter(magazine))
        
        for ele in ransomNote:
            if ele in mg and mg[ele]>0:
                mg[ele] = mg[ele] - 1
            else:
                return False
            
        return True