# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        if n== 0:
            return 0
                        
        def convert_bin(n):
            
            arr = []
            
            while n > 0:
                
                rem = n%2
                arr.append(rem)
                n = n //2
                # print(rem,type(rem))
            
            
            return dict(collections.Counter(arr))[1]
            
        return convert_bin(n)