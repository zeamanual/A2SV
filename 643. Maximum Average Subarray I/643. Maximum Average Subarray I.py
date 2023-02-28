class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        for i  in range(k):
            curr_sum+=nums[i]


        left_ptr = 1
        right_ptr = k
        arr_size = len(nums)
        max_sum = curr_sum
        while(right_ptr<arr_size):
            curr_sum+=nums[right_ptr]
            curr_sum-=nums[left_ptr]
            max_sum = max(curr_sum,max_sum)
            left_ptr+=1
            right_ptr+=1

        
        return max_sum/k
