"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            tmp_level = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp_level.append(node.val)
                for child in node.children:
                    queue.append(child)
            output.append(tmp_level)
        return output