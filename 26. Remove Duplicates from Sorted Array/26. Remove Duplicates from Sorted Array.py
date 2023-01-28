class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if(len(nums)==1):
            return 
        
        left_ptr=0
        right_ptr=1
        k=1
        while(right_ptr<len(nums)):
            if(nums[left_ptr]==nums[right_ptr]):
                right_ptr+=1
            else:
                nums[left_ptr+1]=nums[right_ptr]
                left_ptr+=1
                right_ptr+=1
                k+=1
        return k
