class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        path=path.split('/')
        for path in path:
            if(path=='..' and stack ):
                stack.pop()
            elif(path and path!='.' and path!='..'):
                stack.append(path)

        return '/'+'/'.join(stack)
