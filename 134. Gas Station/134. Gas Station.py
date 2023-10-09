class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if(sum(gas)<sum(cost)):
            return -1
        current_gas=0
        answer = 0
        for i in range(len(gas)):
            current_gas+=gas[i]-cost[i]
            
            if(current_gas<0):
                answer=i+1
                current_gas=0

        return answer
