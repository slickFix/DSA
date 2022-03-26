# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        from collections import Counter
        
        driver_ar = nums2 if len(nums2) <= len(nums1) else nums1
        map_ar = nums2 if len(nums2) > len(nums1) else nums1
        
        mapping = dict(Counter(map_ar))
        
        ret_ar = []
        
        for ele in driver_ar:
            
            if ele in mapping.keys():
                
                if mapping[ele] > 0:
                
                    mapping[ele] = mapping[ele] - 1
                    ret_ar.append(ele)
                    
                    
        return ret_ar