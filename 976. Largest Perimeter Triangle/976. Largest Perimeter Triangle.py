class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums_len = len(nums)
        nums.sort()
        
        answer = 0
        largest_perimeter = -float('inf')

        for i in range(nums_len-2):
            if(nums[i+2]<(nums[i]+nums[i+1])):
                current_perm= nums[i+2]+nums[i]+nums[i+1]
                largest_perimeter=max(largest_perimeter,current_perm)
                answer=largest_perimeter
            
        return answer

                
