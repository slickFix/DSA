#https://leetcode.com/problems/merge-strings-alternately/



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ret_str = ""
        
        for el1,el2 in zip(word1,word2):
            ret_str += el1
            ret_str += el2
            
        if len(word1)<len(word2):
            ret_str += word2[len(word1):]
        if len(word1)>len(word2):
            ret_str += word1[len(word2):]
            
            
        return ret_str
