class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        nums.extend(nums)
        stack = []
        ans = [-1]*size
        for index in range(size*2):
            while( stack and nums[stack[-1]] < nums[index]):
                poped = stack.pop()
                ans[poped]=nums[index]

            stack.append(index%size)

        return ans
