# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if not head:
        return 0
    temp = []
    curr = head
    while curr:
        temp.append(curr)
        curr = curr.next
        if curr in temp:
            return 1
    return 0
