# https://leetcode.com/problems/binary-tree-inorder-traversal/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        
        ret_arr = []
        
        def rec(node,ret_arr):
            
            if node:
                rec(node.left,ret_arr)
                ret_arr.append(node.val)
                rec(node.right,ret_arr)
                
        rec(root,ret_arr)
                
        return ret_arr
            
            
