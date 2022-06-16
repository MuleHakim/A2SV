# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or (head and not head.next):
            return head
        curr = head
        prev = None
        while curr != None and curr.next != None:
            if curr.val == curr.next.val:
                while curr.next != None and curr.val == curr.next.val:
                    curr = curr.next
                if prev != None:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    head = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head
