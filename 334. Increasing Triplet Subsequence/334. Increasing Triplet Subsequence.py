class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        is_valid=False

        for num in nums:
            if(num<=first):
                first=num
            elif(num<=second):
                second = num
            else:
                is_valid=True
                break
        return is_valid
