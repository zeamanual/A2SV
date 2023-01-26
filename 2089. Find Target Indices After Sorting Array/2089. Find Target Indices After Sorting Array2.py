class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        
        answer=[]
        for index in range(len(nums)):
            if(nums[index]==target):
                answer.append(index)

        return answer
