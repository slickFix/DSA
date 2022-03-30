# https://leetcode.com/problems/n-ary-tree-preorder-traversal/


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ret_arr = []
        if root is None:
            return ret_arr
        
        def pre_order(node):
            
            
            ret_arr.append(node.val)
            
            for child in node.children:
                pre_order(child)
            
        pre_order(root)
        
        return ret_arr