class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total_sum = sum(nums)

        if(total_sum%2!=0):
            return False
            
        cache = dict()
        def dp(ptr,target):

            if((ptr,target) in cache):
                return cache[(ptr,target)]
            if target==0:
                return True

            if(ptr==len(nums) or target<0):
                return False
            
            cache[(ptr,target)]=dp(ptr+1,target) or dp(ptr+1,target-nums[ptr])
            return cache[(ptr,target)]

        return dp(0,total_sum//2)
