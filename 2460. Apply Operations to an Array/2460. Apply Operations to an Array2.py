class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        nums_size = len(nums)

        for index in range(nums_size-1):
            if(nums[index]==nums[index+1]):
                nums[index]*=2
                nums[index+1]=0
        ptr=0
        i=0
        while(ptr<nums_size and i<nums_size):
            if(nums[i]==0 and i<nums_size-1):
                ptr=max(i,ptr)
                while(ptr<nums_size and nums[ptr]==0):
                    ptr+=1
                if(ptr<nums_size):
                    nums[i],nums[ptr]=nums[ptr],nums[i]
            i+=1

        return nums
