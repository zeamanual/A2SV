class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def dp(p1,p2):

            if(len(word1)==p1):
                return len(word2)-p2

            if(len(word2)==p2):
                return len(word1)-p1

            if(word1[p1]==word2[p2]):
                return dp(p1+1,p2+1)
            else:
                replace = 1 + dp(p1+1,p2+1)
                insert = 1 + dp(p1,p2+1)
                delete = 1 + dp(p1+1,p2)
                return min(replace,insert,delete)

        return dp(0,0)
