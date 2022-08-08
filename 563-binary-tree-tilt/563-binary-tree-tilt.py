# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        output = 0
        def total(root) -> None:
            nonlocal output
            if not root:
                return 0
            left = total(root.left)
            right = total(root.right)
            output += abs(left - right)
            return root.val + left + right
        total(root)
        return output