# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ind_map = {ele:ind for ind,ele in enumerate(nums2)}
        
        ret_arr = []
        
        
        for ele in nums1:
            
            ind = ind_map[ele]
            
            for i in range(ind+1,len(nums2)):
                if nums2[i] > ele:
                    ret_arr.append(nums2[i])
                    break
            else:
                ret_arr.append(-1)
                
        return ret_arr