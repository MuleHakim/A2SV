# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = []
        maxTotal = 0
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        i = 0
        j = len(temp)-1
        while i<j:
            total = temp[i]+temp[j]
            maxTotal = max(maxTotal,total)
            i += 1
            j -= 1
        return maxTotal