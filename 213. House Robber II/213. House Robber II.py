class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache(None)
        def get_max(curr,index,robbed=False):

            if(index >= len(nums)):
                return curr

            if(index==len(nums)-1 and robbed):
                return curr
        
            # 1
            sum1 =  get_max(curr + nums[index],index + 2, True if index ==0 else robbed)

            #2
            sum2 =  get_max(curr,index + 1,robbed)

            return max(sum1,sum2)

        return get_max(0,0)
