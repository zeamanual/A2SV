class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
       
        houses.sort()
        heaters.sort()

        answer = 0
        for house in houses:
            left= bisect_right(heaters,house)
            right = bisect_left(heaters,house)
            if(left==0 or right ==len(heaters)):
                if(left==0):
                    answer = max(answer,abs(house-heaters[0]))
                else:
                    answer = max(answer,abs(house-heaters[-1]))
            else:
                answer = max(answer,min(abs(house-heaters[left-1]),abs(house-heaters[right])))

        return answer
