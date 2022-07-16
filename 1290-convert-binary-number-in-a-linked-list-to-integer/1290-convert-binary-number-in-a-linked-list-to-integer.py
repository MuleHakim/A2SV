# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = []
        output = 0
        curr = head
        while curr!=None:
            temp.append(curr.val)
            curr = curr.next
        temp = temp[::-1]
        for i in range(len(temp)):
            output += 2**i * temp[i]
        return output