class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index = 0
        ans = []
        while(index<len(nums)):
            pos = nums[index]-1
            if(nums[pos]==nums[index] and pos!=index and nums[index]!=-1):
                ans.append(nums[index])
                nums[index]=-1
                index+=1
            elif(nums[index]==-1):
                index+=1
            else:
                nums[pos],nums[index]=nums[index],nums[pos]
                index+=1 if index==pos else 0

        for index in range(len(nums)):
            if(nums[index]==-1):
                ans.append(index+1)
                break
        

        return ans
