# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        from collections import Counter
        
        mapping = dict(Counter(s))
        
        for index,el in enumerate(s):
            if mapping[el] == 1:
                return index
        
        return -1