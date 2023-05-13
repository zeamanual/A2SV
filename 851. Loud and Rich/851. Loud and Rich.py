class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        adj = defaultdict(set)
        poorer_count = [0 for i in range(len(quiet))]
        for rich,poor in richer:
            adj[rich].add(poor)
            poorer_count[poor]+=1

        que = deque()
        for person in range(len(quiet)):
            if(poorer_count[person]==0):
                que.append(person)
                
        result = [index for index in range(len(quiet))]
        while(que):
            
            quitest = que.popleft()
            for poor in adj[quitest]:
                if(quiet[result[quitest]]<=quiet[result[poor]]):
                    result[poor]=result[quitest]

                poorer_count[poor]-=1
                if(poorer_count[poor]==0):
                    que.append(poor)

        return result
