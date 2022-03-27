# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        from collections import Counter
        def check_dups(arr):
            
            mapping = dict(Counter(arr))
            
            for i in range(1,10):
                ele = str(i)
                if ele in mapping.keys() and mapping[ele] > 1:
                    return False
                
            return True
            
        for i in range(len(board)):
            boo = check_dups(board[i])
            if boo is False:
                return False
            
        for i in range(len(board)):
            boo = check_dups(  [ele[i] for ele in board] )
            if boo is False:
                return False
            
        for i in range(0,len(board),3):
            
            for j in range(0,len(board),3):
                arr = []
                for k in range(3):
                    for l in range(3):
                        
                        arr.append(board[i+k][j+l])
                        
                        
                boo = check_dups(arr)
                if boo is False:
                    return False
                                        
        return True