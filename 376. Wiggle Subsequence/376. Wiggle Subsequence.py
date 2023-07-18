class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        if(len(nums)<2):
            return len(nums)

        max_length = 1
        last_sign = 0

        for i in range(1,len(nums)):
            if(last_sign ==0 ):
                last_sign = 1 if nums[i]-nums[i-1] else -1

            if((nums[i]-nums[i-1] > 0 and last_sign==-1 ) or (nums[i]-nums[i-1] <  0 and last_sign==1)):
                max_length+=1
                last_sign = 1 if nums[i]-nums[i-1] else -1

        
        return max_length
