class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        nums_cp=nums.copy()
        nums.sort()


        sorted_pos={}
        for index,num in enumerate(nums):
            if(num not in sorted_pos):
                sorted_pos[num]=index
        
        final_ans=[]
        for num in nums_cp:
            final_ans.append(sorted_pos[num])

        return final_ans
