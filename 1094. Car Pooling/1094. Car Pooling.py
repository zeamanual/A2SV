class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_span = [0 for i in range(10001)]

        for trip in trips:
            trip_span[trip[1]]+=trip[0]
            trip_span[trip[2]]-=trip[0]

        for i in range(1,len(trip_span)):
            trip_span[i]+=trip_span[i-1]

        for trip in trips:
            if(trip_span[trip[1]]>capacity or trip_span[trip[2]] >capacity):
                return False
        

        return True
