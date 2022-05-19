# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pos = -1
        myStack = []
        output = []
        left  = head
        while left:
            pos += 1
            output.append(0)
            while myStack and myStack[-1][1] < left.val:
                index,value= myStack.pop()
                output[index] = left.val
            myStack.append((pos,left.val))
            left = left.next
        return output
    
        # myStack = []
        # left = head
        # while left.next:
        #     myStack.append(left.val)
        #     left = left.next
        # myStack.append(left.val)
        # i = 0
        # j = 1
        # output = []
        # while i<j:
        #     if j<len(myStack) and myStack[i] < myStack[j]:
        #         output.append(myStack[j])
        #         i += 1
        #         j = i + 1
        #     elif j==len(myStack):
        #         output.append(0)
        #         i += 1
        #         if len(output)==j:
        #             break
        #         j = i + 1
        #     elif i==len(myStack)-1:
        #         output.append(0)
        #         break
        #     else:
        #         j += 1
        # return output