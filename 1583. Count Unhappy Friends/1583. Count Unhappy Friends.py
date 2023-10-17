class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        

        better_prefs = defaultdict(list)
        for pair1,pair2 in pairs:
            better_prefs[pair1]=set(preferences[pair1][:preferences[pair1].index(pair2)])
            better_prefs[pair2]=set(preferences[pair2][:preferences[pair2].index(pair1)])
        
        answer = 0
        for person_id in better_prefs:
            
            for candidate in better_prefs[person_id]:
                if(person_id in better_prefs[candidate]):
                    answer+=1
                    break

        return answer
