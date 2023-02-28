class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        que = deque(tickets)
        time = 0
        while(que[k]>0):
            for i in range(len(que)):
                time_to_buy = 1 if que[i]>0 else 0
                que[i]-=time_to_buy
                time +=time_to_buy
                if(que[k]<1):
                    break
                
        return time

    
