# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        pos = []
        for ind,(one,two) in enumerate(zip(s1,s2)):            
            if one != two:            
                pos.append(ind)
        
        if len(pos) == 0 :
            return True
        elif len(pos) != 2 :
            return False
        else:            
            if s1[pos[0]] == s2[pos[1]] and s1[pos[1]] == s2[pos[0]]:
                return True
            else:
                return False
            