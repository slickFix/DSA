# https://leetcode.com/problems/merge-two-sorted-lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = tmp = ListNode(0)
        
        
        while list1 and list2:
            
            if list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
                
            tmp = tmp.next
            #print(tmp.val)
            
        if not list1 and not list2:
            return None
        
        if list1:
            tmp.next = list1
        else:
            tmp.next = list2
            
        return head.next
        
        
        
        
#         if list1 is None:
#             return list2
#         if list2 is None:
#             return list1
        
#         h1 = list1
#         h2 = list2
        
          ## FAILS FOR 1 2 3 | 2 3 4  CASE !!
#         while list1 and list2 :
            
#             small = list1 if list1.val <= list2.val else list2
#             big = list2 if list1.val <= list2.val else list1
            
#             if small.next :
#                 if small.next.val <= big.val:
#                     if small == list1:
#                         list1 = list1.next
#                     else:
#                         list2 = list2.next
#                 else:
#                     if small == list1:
#                         list1 = list1.next
#                     else:
#                         list2 = list2.next
#                     small.next = big
                
#             else:
#                 small.next = big
#                 break
            
            
#         return h1 if h1.val<=h2.val else h2
        
        
        
        
#         while list1 and list2:
            
#             if list1.val <= list2.val:
#                 if list1.next is not None and list1.next.val < list2.val :
#                     list1 = list2.next
                    
#                 else:
#                     tmp = list1.next
#                     list1.next = list2
#                     list1 = tmp
#             elif list2.next is not None and list2.next.val < list1.val:
#                 list2 = list2.next
#             else:
#                 tmp = list2.next
#                 list2.next = list1
#                 list2 = tmp
                
                
        
                
#         return h1 if h1.val<=h2.val else h2
            
