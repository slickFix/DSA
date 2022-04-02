# https://leetcode.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # recursive
        if not head:
            return None
                            
        if head.val == val:
            return self.removeElements(head.next,val)
        else:
            head.next =  self.removeElements(head.next,val)
            return head
        

        # iterative
        h = curr = ListNode(0)
        
        while head:
            
            if head.val != val:
                curr.next = head
                curr = curr.next
            else:
                curr.next = None
            
            head = head.next            
            
            
        return h.next
        
#         while head.val == val:
#             head = head.next
#             if head is None:
#                 return None
            
            
#         tmp = head 
#         nxt = head.next
        
#         while nxt:
#             flag = False
#             while nxt.val == val:
#                 nxt = nxt.next
#                 flag = True                
        
#             if flag:
#                 tmp.next = nxt
#             else:
#                 nxt = nxt.next
#                 tmp = tmp.next 
                
        
#         return head
