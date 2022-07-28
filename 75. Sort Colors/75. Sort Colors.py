class Solution(object):
    def sortColors(self, nums):
        size = len(nums)
        for index in range(1,size):
            temp_index=index
            while(nums[temp_index]<nums[temp_index-1] and temp_index > 0):
                nums[temp_index],nums[temp_index-1]=nums[temp_index-1],nums[temp_index]
                temp_index-=1
        
