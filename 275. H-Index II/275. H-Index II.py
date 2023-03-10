class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left =0
        right = len(citations)-1
        h=0
        size = len(citations)

        while(left<=right):
            
            mid = left+(right-left)//2
            above_current = size-mid
            if( citations[mid]>=above_current):
                h=max(h,above_current)
                right=mid-1

            else:
                left=mid+1

        return h
