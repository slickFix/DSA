# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr = head
        move = head.next
        
        
        while move:
            
            if move.val == curr.val:
                move = move.next
            else:
                curr.next = move
                curr = move
                move = move.next
                
        curr.next = move ## repeating for case like 1,1,2,3,3 (required for 3,3)

        return head
            
