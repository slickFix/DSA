# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ret_arr = []
        
        last_row = [1]
        
        if numRows == 1:
            ret_arr.append(last_row)
            return ret_arr
            
        else:
            
            ret_arr.append(last_row)
                        
            for i in range(1,numRows):
                new_row = [1] * (len(ret_arr[-1]) +1)
                
                pre_row = ret_arr[-1]
                
                for ind in range(1,len(new_row)-1):
                    
                    new_row[ind] = pre_row[ind-1] + pre_row[ind]
                    
                ret_arr.append(new_row)
                
            return ret_arr