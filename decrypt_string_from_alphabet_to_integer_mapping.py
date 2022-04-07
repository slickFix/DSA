# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/


class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        di = {str(i):chr(ord('a')+i-1) for i in range(1,10)}
        di.update({str(i)+"#":chr(ord('a')+i-1) for i in range(10,27) })
        
        ret_str = ''
        
        #print(di)
        
        li = list(s)
        
        while li:
            
            if li[-1] =="#":
                ret_str += di["".join(li[-3:])]
                
                li.pop()
                li.pop()
                li.pop()
            else:
                #print(li[-1])
                ret_str += di[li[-1]]  
                li.pop()
        
        return ret_str[::-1]
