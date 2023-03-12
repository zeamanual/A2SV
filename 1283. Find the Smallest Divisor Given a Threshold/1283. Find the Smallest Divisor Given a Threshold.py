class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        left = 1
        right = 1000000
        ans = float('inf')

        while(left <= right):
            middle = left + (right -left)//2
            curr_result = self.calculate_sum(middle,nums)
            if(curr_result <= threshold):
                ans = min(ans,middle)
                right = middle-1
            else:
                left = middle+1
        
        return ans


    def calculate_sum (self,devider,nums):

        curr_sum = 0
        for num in nums:
            curr_sum += (ceil(num/devider))

        return curr_sum
