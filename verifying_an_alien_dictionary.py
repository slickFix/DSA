# https://leetcode.com/problems/verifying-an-alien-dictionary/



class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        

        
        di = {el:ind for ind,el in enumerate(order)}
        ind = 0
        
        for i in range(1, len(words)):
            
            prev, curr, flag = words[i-1],words[i],0            

                        
            for j in range(min(len(prev),len(curr))):
                
                # print(prev,curr,j)
                
                if di[prev[j]] < di[curr[j]]:
                    flag = 1
                    break
                elif di[prev[j]] > di[curr[j]]:
                    return False
            
            if not flag and len(prev)> len(curr):
                return False
            
        return True
            
        
