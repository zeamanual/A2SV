class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        copied = intervals.copy()
        intervals = [[value[0],value[1],index]   for index, value in enumerate(intervals)]
        intervals.sort(key=lambda val:val[0])
        size = len(intervals)
        answer = []
        for interval in copied:
            left = 0 
            right = size-1
            ans = -1
            while(left<=right):
                middle = left + (right - left )//2

                if(intervals[middle][0]>=interval[1]):
                    ans = intervals[middle][2]
                    right = middle-1
                else:
                    left = middle+1

            answer.append(ans)

        return answer
