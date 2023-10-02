class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for char in s:

            if(not stack):
                stack.append((char,1))
            else:

                count = stack[-1][1]+1 if char == stack[-1][0] else 1
                stack.append((char,count))
                
                if(stack[-1][1]==k):
                    while(stack and stack[-1][0]==char):
                        stack.pop()

        answer = ''
        for char,count in stack:
            answer += char

        return answer
