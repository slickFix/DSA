# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        t_sum = sum(arr)
        
        for le in range(3,len(arr)+1,2):
            tmp_s = 0

            for j in range(len(arr)-le+1):

                tmp_s += sum(arr[j:j+le])
            t_sum += tmp_s
            
        return t_sum