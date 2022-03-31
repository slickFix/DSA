# https://leetcode.com/problems/matrix-diagonal-sum/


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        p_sum = sum([mat[i][i] for i in range(len(mat))])
        s_sum = sum([mat[len(mat)-i-1][i] for i in range(len(mat))])
        
        if len(mat)%2 != 0:
            return p_sum + s_sum - mat[len(mat)//2][len(mat)//2]
        else:
            return p_sum + s_sum
