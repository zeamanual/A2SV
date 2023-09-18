class Solution:
    def minSteps(self, n: int) -> int:

        @lru_cache(None)
        def helper(count,clipboard):

            print(count,clipboard)
            if(count>n or clipboard>n):
                return float('inf')
            elif(count==n):
                return 0

            coping_result = 2 + helper(count*2,count)
            pasting_result = 1+ helper(count+clipboard,clipboard) if clipboard else float('inf')
            return min(coping_result,pasting_result)

        return helper(1,0)
