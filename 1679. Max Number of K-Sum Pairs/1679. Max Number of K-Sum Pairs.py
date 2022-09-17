import math
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = {}
        maxOperations= 0
        for number in nums:
            if(counts.get(number)==None):
                counts[number]=1
            else:
                counts[number]+=1
        for number in counts.keys():
            if(number in counts.keys() and k-number in counts.keys()):
                if(number == k/2):
                    maxOperations+= math.floor(counts[number]/2)
                    counts[number]=0
                    counts[k-number]=0
                else:
                    maxOperations+=min(counts[number],counts[k-number])
                    counts[number]=0
                    counts[k-number]=0
        return maxOperations
                    
