# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or head.next==None:
            return True
        else:
            right = head
            left = head
            stack = []
            while right and right.next:
                stack.append(left.val)
                left = left.next
                right = right.next.next

            if right:
                left = left.next

            while left:
                if left.val != stack.pop():
                    return False
                else:
                    left = left.next

            return True
