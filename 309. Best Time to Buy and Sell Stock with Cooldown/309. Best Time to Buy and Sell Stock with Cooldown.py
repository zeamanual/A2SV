class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dp(index,curr_stock):
            
            if(index>=len(prices)):
                return 0

            maximum_possible = [float('-inf') for i in range(4)]
            if(not curr_stock):

                # buying current day stock
                maximum_possible[0]=-prices[index]+dp(index+1,True)
                
                # doing nothing
                maximum_possible[1]=dp(index+1,False)
            
            else:
                # selling it today
                maximum_possible[2] = prices[index]+dp(index+2,False)
                # keep it 
                maximum_possible[3] = dp(index+1,True)

            return max(maximum_possible)

        return dp(0,False)
