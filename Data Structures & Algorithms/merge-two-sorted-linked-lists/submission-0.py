# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        
        p1,p2 = list1,list2
        newlist = dummy = ListNode()
        while p1 and p2:
            if p1.val < p2.val:
                newlist.next = p1
                p1 = p1.next
            else:
                newlist.next = p2
                p2 = p2.next
            newlist = newlist.next
        
        if p1 and not p2:
            newlist.next = p1
        else:
            newlist.next = p2
        
        return dummy.next