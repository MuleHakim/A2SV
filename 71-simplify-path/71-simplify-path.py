class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for i in path:
            if i in ['', '.']:
                continue
            if i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        output = '/'.join(stack)
        return '/' + output