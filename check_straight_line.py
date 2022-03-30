# https://leetcode.com/problems/check-if-it-is-a-straight-line/


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]
        
        
        if x2-x1 == 0 :
            x_cord = set([coord[0] for coord in coordinates])
            
            if len(x_cord) == 1:
                return True
            else:
                return False
            
        
        m = (y2-y1)/(x2-x1)
        
        # y-y1 = m(x-x1)
        
        for x_i,y_i in coordinates[2:]:
            
            if y_i != m*(x_i - x1)+y1:
                return False
            
        return True