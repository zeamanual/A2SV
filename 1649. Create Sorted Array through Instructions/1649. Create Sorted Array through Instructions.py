from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:

        cost = 0
        nums = SortedList()
        freq = dict()

        for num in instructions:
            option1 =  nums.bisect_left(num)
            option2 = len(nums) - nums.bisect_right(num)
            cost = (cost + min(option1, option2))%(10**9+7)
            nums.add(num)
            freq[num] = freq.get(num,0)+1

        return cost
