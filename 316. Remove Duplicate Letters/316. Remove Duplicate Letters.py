class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = {}

        for char in s:
            count[char]=count.get(char,0)+1

        stack = []
        added = set()

        for char in s:
            if(char not in added):
                while(stack and stack[-1] > char and count[stack[-1]]>0):
                    removed = stack.pop()
                    added.discard(removed)

                stack.append(char)
                added.add(char)
                
            count[char]-=1

        return ''.join(stack)
