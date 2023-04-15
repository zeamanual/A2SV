class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        index = 0
        size = len(nums)

        while(index<size):
            pos = nums[index]-1

            if(pos == index):
                index+=1
            else:
                if(nums[pos]==nums[index]):
                    return nums[pos]
                nums[pos],nums[index]=nums[index],nums[pos]
