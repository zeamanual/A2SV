class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        size = len(nums)
        index=0
        while(index < size):
            if(nums[index]==size):
                nums[index]=-1
                index+=1
            elif(nums[index]==-1):
                index+=1
            else:
                pos = nums[index]
                nums[index],nums[pos]=nums[pos],nums[index]
                if(pos==index):
                    index+=1

        for index in range(size):
            if(nums[index]==-1):
                return index

        return size
