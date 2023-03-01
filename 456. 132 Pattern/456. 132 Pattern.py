class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second_largest = float('-inf')

        stack = []

        for index in range(len(nums)-1,-1,-1):
            num = nums[index]
            if(num<second_largest):
                return True

            while(stack and stack[-1]<num):
                second_largest=stack.pop()

            stack.append(num)

        return False
