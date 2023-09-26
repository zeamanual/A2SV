class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        n=len(stones)
        weightSum = sum(stones)
        target = weightSum//2

        @lru_cache(None)
        def helper(index,currentTotal):

            if(currentTotal>=target or index==n):
                return abs(currentTotal-(weightSum-currentTotal))
            
            return min(helper(index+1,currentTotal+stones[index]),helper(index+1,currentTotal))


        return helper(0,0)
