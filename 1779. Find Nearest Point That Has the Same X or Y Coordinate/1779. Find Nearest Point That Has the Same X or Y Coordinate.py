class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        closest_index=-1
        closest_distance=float('inf')
        for index,pt in enumerate(points):
            if(pt[0]==x or pt[1]==y):
                current_distance=abs(x-pt[0])+abs(y-pt[1])
                if(current_distance<closest_distance):
                    closest_index=index
                    closest_distance=current_distance
        return closest_index
