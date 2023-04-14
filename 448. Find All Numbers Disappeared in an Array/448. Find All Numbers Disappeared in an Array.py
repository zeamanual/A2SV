class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        size = len(nums)
        index=0
        while(index<size):
            pos = nums[index]-1
            if(nums[pos] != nums[index]):
                nums[pos],nums[index] = nums[index],nums[pos]
            else:
                index+=1

        answer = []

        for i in range(size):
            if(nums[i]-1 != i):
                answer.append(i+1)

        return answer
