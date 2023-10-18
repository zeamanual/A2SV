class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        if(len(nums)<2):
            return 0
        
        even_freq= defaultdict(int)
        odd_freq= defaultdict(int)
        for i,num in enumerate(nums):
            if(i%2==0):
                even_freq[num]+=1
            else:
                odd_freq[num]+=1

        evens =[(even_freq[key],key) for key in even_freq.keys()]
        odds =[(odd_freq[key],key) for key in odd_freq.keys()]
        evens.sort()
        odds.sort()

        if(evens[-1][1]==odds[-1][1]):
            result = float('inf')
            if(len(evens)==len(odds)==1):
                return min(evens[-1][0],odds[-1][0])
            if(len(evens)>1):
                result = min(result, len(nums)-evens[-2][0] -odds[-1][0])
            if(len(odds)>1):
                result = min(result, len(nums)-evens[-1][0] -odds[-2][0])
            
            return result
        else:
            return len(nums)-evens[-1][0]-odds[-1][0]
