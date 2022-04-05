# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        mapp = dict(collections.Counter(list(t)))
        
        for e in s:
            if e in mapp:
                mapp[e]-=1
        
        return [el for el,val in mapp.items() if val ==1][0]
