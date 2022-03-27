# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        
        min_sal = min(salary)
        max_sal = max(salary)
        
        tot_sal = sum(salary)
        
        return (tot_sal-min_sal-max_sal)/(len(salary)-2)