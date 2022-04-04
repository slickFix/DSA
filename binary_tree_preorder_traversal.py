# https://leetcode.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ret_arr = []
        
        if root is None:
            return ret_arr
        
        
        def rec(root,ret_arr):
            
            if root is None:
                return
            
            ret_arr.append(root.val)
            
            rec(root.left,ret_arr)
            rec(root.right,ret_arr)
            
        rec(root,ret_arr)
            
        return ret_arr
