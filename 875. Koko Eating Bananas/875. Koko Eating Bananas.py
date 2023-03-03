class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed= float('inf')
        max_speed = float('-inf')

        for pile in piles:
            min_speed = min(min_speed,pile)
            max_speed = max(max_speed,pile)

        left = 1
        right = max_speed
        ans = float('inf')
        while(left<=right):
            mid = left + (right-left)//2
            curr_hour=0
            for pile in piles:
                curr_hour+=ceil(pile/mid)

            if(curr_hour>h):
                left=mid+1
            else:
                ans=mid
                right=mid-1

        return ans

