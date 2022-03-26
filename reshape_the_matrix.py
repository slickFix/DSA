# https://leetcode.com/problems/reshape-the-matrix/submissions/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        ac_r = len(mat)
        ac_c = len(mat[0])
        
        if ac_r * ac_c == r *c:
            
            ret_arr = []
            row_ele = []
            
            for i in range(ac_r):
                for j in range(ac_c):
                    ele = mat[i][j]
                    
                    if len(row_ele) < c:                                            
                        row_ele.append(ele)
                    
                    else:
                        row_ele = []
                        row_ele.append(ele)
                        
                    if len(row_ele) == c:
                        ret_arr.append(row_ele)
            
            return ret_arr
            
        else:
            return mat