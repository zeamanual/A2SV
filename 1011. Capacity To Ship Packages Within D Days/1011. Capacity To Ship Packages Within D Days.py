class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lowest,highest,ans = 1, 500*50000,float('inf')
        while(lowest<=highest):

            curr_weight = lowest+(highest-lowest)//2
            curr_days,size,ptr,weight = 1,len(weights),0,0
            while(ptr<size):
                
                weight+=weights[ptr]
                if(weight>curr_weight):
                    curr_days+=1
                    weight=weights[ptr]
                ptr+=1

            if(curr_days<=days):
                highest=curr_weight-1
                ans = curr_weight
            else:
                lowest=curr_weight+1

        return ans
