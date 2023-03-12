class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):

        self.persons = persons
        self.times = times
        status  = defaultdict(int)
        self.answer = []
        leader = persons[0]
        for index in range(len(persons)):
            status[persons[index]]+=1
        
            if( status[persons[index]] >= status[leader] ):
                leader = persons[index]
            self.answer.append(leader)


    def q(self, t: int) -> int:

        return self.answer[self.helper(t)]

    def helper(self,required_time):
        left = 0
        right = len(self.times)-1
        ans = float('-inf')
        while(left<=right):
            middle = left + (right-left)//2

            if(self.times[middle]<=required_time):
                ans = max(ans,middle)
                left = middle + 1
            else:
                right = middle - 1

        return ans

           

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
