class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        
        bit_result = nums[0]

        for num in nums:
            bit_result &= num
        # print(bit_result)
        if(bit_result != 0):
            return 1
        else:
            count =0
            temp =nums[0]
            for index,num in enumerate(nums):
                temp&=num
                if(temp==0):
                    count+=1
                    temp= nums[index+1] if index<len(nums)-1 else 0
                    # print(num,count)

            return count
