import math
class Solution(object):
    def kClosest(self, points, k):
        size=len(points)
        distance_list =[]
        for pt in points:
            distance = math.sqrt((pt[0]**2+pt[1]**2))
            distance_list.append([distance,pt])
        distance_list.sort()
        
        selected_pts = distance_list[0:k]
        answer = []
        for pt in selected_pts:
            answer.append(pt[1])
            
        return answer
        
