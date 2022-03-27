# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        r = len(matrix)
        c = len(matrix[0])
        
        
        def b_search(col, c):
            
            start = 0
            end = c -1

            while start<=end:
                
                mid = (start + end)//2
                
                if col[mid] == target:
                    return True
                elif col[mid] >target:                        
                    end = mid -1                
                    #print(start,mid,end)

                elif col[mid]< target:
                    start = mid + 1
                    
            return False
        
        if r==1 :
            
            if c ==1 and matrix[0][0] == target:
                return True
            elif c == 1 and matrix[0][0] != target:
                return False
            
            col = matrix[0]
                     
            return b_search(col,c)
            
        
        for i in range(r-1):
            
            if target>= matrix[i][0] and target< matrix[i+1][0]:
                col = matrix[i]
                
                #print(col)
                
                
                return b_search(col,c)
        
        return b_search(matrix[-1],c)
                
                
                
            