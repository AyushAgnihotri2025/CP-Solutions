class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for directory in path.split('/'):
            if directory == '' or directory == '.':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        return '/' + '/'.join(stack)