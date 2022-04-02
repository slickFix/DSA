# https://leetcode.com/problems/reverse-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        curr = tmp = head
        back = None
        
        while curr:
            tmp = curr
            
            curr = curr.next
            tmp.next = back
            back = tmp
            
            
            
        return tmp
