# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a_pointer = headA
        b_pointer = headB
        while a_pointer != b_pointer:
            if a_pointer==None:
                a_pointer = headB
            else:
                a_pointer = a_pointer.next
            if b_pointer==None:
                b_pointer = headA
            else:
                b_pointer = b_pointer.next
        return a_pointer