# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pred = None
        x = None  # 1st wrong node
        y = None  # 2nd wrong node
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if not x:
                    x = pred
            pred = root
            root = root.right

        def swap(x: Optional[TreeNode], y: Optional[TreeNode]) -> None:
            temp = x.val
            x.val = y.val
            y.val = temp
        swap(x, y)