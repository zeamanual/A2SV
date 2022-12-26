class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        nums_len = len(nums)
        good_pairs=0
        
        for i in range(nums_len):
            current_num=nums[i]
            for j in range(i+1,nums_len):
                if(current_num==nums[j]):
                    good_pairs+=1
            
        return good_pairs
                    
