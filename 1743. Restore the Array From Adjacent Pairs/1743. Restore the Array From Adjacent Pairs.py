class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for pair in adjacentPairs:
            adj[pair[0]].append(pair[1])
            adj[pair[1]].append(pair[0])

        edge_element = 0

        for num in adj.keys():
            if(len(adj[num])==1):
                edge_element = num
                break
        
        visited = set()
        answer = []
        def dfs(node):
            nonlocal answer
            nonlocal visited
            visited.add(node)
            answer.append(node)

            for nbr in adj[node]:
                if(nbr not in visited):
                    dfs(nbr)

        dfs(edge_element)
        return answer                
