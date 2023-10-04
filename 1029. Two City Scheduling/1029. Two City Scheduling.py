class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
       
        priorites = []
        n=len(costs)

        for index,cost in enumerate(costs):
            priorites.append((abs(cost[0]-cost[1]),index))

        priorites.sort(reverse=True)

        city_a,city_b=[],[]
        for priority in priorites:

            curr_person = priority[1]
            if( len(city_b)==n//2 or ( costs[curr_person][0]<costs[curr_person][1] and len(city_a)<n//2)):
                city_a.append(costs[curr_person][0])
            else:
                city_b.append(costs[curr_person][1])

        return sum(city_a+city_b)
