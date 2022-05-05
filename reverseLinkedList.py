# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            pre = None
            while head != None:
                next_node = head.next
                head.next = pre
                pre = head
                head = next_node

            return pre
