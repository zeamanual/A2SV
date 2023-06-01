class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @lru_cache(None)
        def get_max(index,flag):
            if(index>=len(prices)):
                return 0
            if(flag):
                # flagged
                option1 = prices[index]-fee + get_max(index+1,False)

                option2 = get_max(index+1,flag)

                return max(option1,option2)
            else:
                # not flagged
                option3 = -prices[index] + get_max(index+1,True)
                option4 = get_max(index+1,False)

                return max(option3,option4)

        return get_max(0,False)
