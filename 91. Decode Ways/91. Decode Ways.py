class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def get_max(index):

            if(index<len(s) and s[index]=='0'):
                return 0

            if(index+1>=len(s)):
                return 1
            else:
                option1 = get_max(index+1)
                option2 = 0
                if(int(s[index:index+2])<=26):
                    option2 = get_max(index+2)
                return option1+option2

        return get_max(0)
