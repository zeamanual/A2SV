class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        @lru_cache(None)
        def dp(ptr,last_pass):

            if(ptr>=len(days)):
                return 0

            if(days[ptr]<=last_pass):
                return dp(ptr+1,last_pass)
            else:
                result = min(
                    costs[0] + dp(ptr+1,days[ptr]),
                    costs[1]+ dp(ptr+1,days[ptr]+6),
                    costs[2]+ dp(ptr+1,days[ptr]+29),
                )
                return result

        return dp(0,-1)
