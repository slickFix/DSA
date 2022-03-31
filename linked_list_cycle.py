# https://leetcode.com/problems/linked-list-cycle/submissions/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None :
            return False
        
        n = head
        nn = head.next

        
        while nn is not n:
            
            n = n.next
            
            if nn is not None and nn.next is not None:
                nn = nn.next.next
            else:
                return False
                
            
        return True