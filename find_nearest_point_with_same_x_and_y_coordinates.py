# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        valid_pts = []
        
        for ind,pt in enumerate(points):
            
            x_i,y_i = pt[0],pt[1]
            
            if x_i == x or y_i == y:
                pt.append(ind)
                valid_pts.append(pt)

        
        if len(valid_pts) == 0:
            return -1
        else:
            min_dis = sys.maxsize
            ind = -1            
            
            for ele in valid_pts:
                x_i,y_i,local_ind = ele
                dis  = abs(x-x_i) + abs(y-y_i)
                
                if dis < min_dis :
                    min_dis = dis
                    ind = local_ind

        
            return ind 