class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre,i, j = None, head, head
        while j and j.next:
            pre, i, j = i, i.next, j.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(i))

    def merge(self, left, right):
        dummy = tail = ListNode()
        while left and right:
            if left.val < right.val:
                tail.next, tail, left = left, left, left.next
            else:
                tail.next, tail, right = right, right, right.next
        tail.next = left or right
        return dummy.next
