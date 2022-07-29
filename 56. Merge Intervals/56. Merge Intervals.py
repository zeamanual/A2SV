class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        new_intervals=[]
        for interval in intervals:
            if(len(new_intervals) < 1 or not self.exists(interval[0],new_intervals[-1])):
                new_intervals.append(interval)
                
            else:
                new_intervals[-1][1]=max(new_intervals[-1][1],interval[1])
        return new_intervals
        
    def exists(self,target,interval):
        if(target >= interval[0] and target <= interval[1]):
            return True
        else:
            return False
        
