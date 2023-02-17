class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        decoded=''

        for char in s:
            if(char!=']'):
                stack.append(char)
            else:
                poped=''
                temp=stack.pop()
                while(temp!='['):
                    poped=temp+poped
                    temp=stack.pop()

                temp=stack.pop()
                num=''

                stack_empty=False
                while(temp.isdigit() and not stack_empty):
                    num=temp+num
                    if(not stack):
                        stack_empty = True
                    else:
                        temp=stack.pop()

                if(not stack_empty):
                    stack.append(temp)


                for i in range(int(num)):
                    stack.extend(list(poped))
   
        return ''.join(stack)
