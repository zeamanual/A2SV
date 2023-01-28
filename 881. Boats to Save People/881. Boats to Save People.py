class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numberOfBoats = 0
        leftPtr = 0
        rightPtr = len(people)-1
        people.sort()

        while leftPtr <= rightPtr:
            if people[leftPtr] + people[rightPtr] <= limit:
                leftPtr += 1
                rightPtr -= 1
            else:
                rightPtr -= 1
            numberOfBoats += 1

        return numberOfBoats
