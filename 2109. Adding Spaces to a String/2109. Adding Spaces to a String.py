class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        if(len(spaces)<1):
            return s

        result = ''
        s_len = len(s)
        ptr=0
        spaces_len = len(spaces)

        for i in range(s_len):
            if( ptr<spaces_len and spaces[ptr]==i):
                result+=' '
                ptr+=1

            result+=s[i]

        return result
