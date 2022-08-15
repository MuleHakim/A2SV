# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def rec(n, p, gp):
            if not n: return 0
            ans = 0
            if gp == 0:
                ans += n.val
            ans += rec(n.left, n.val % 2, p)
            ans += rec(n.right, n.val % 2, p)
            return ans 
        return rec(root, 1, 1)
