"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        output = 0
        for child in root.children:
            tmp = self.maxDepth(child)
            if tmp > output:
                output = tmp
        return 1 + output
