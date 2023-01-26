class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq_count = [0,0,0]

        for num in nums:
            freq_count[num]+=1
        
        count_index=0
        for index, freq in enumerate(freq_count):
            while(freq_count[index]>0):
                nums[count_index]=index
                freq_count[index]-=1
                count_index+=1
        
