class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()

        @lru_cache(None)
        def helper(index,count):
            if(index==len(satisfaction)):
                return 0

            # including current dish
            pick = (count+1)*satisfaction[index] + helper(index+1,count+1)

            # jumping current dish 
            dont_pick = helper(index+1,count)
            return max(pick,dont_pick)

        
        return helper(0,0)
