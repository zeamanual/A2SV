class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:

        graph  = defaultdict(list)

        # constructing adj list
        for node in range(len(parent)):
            if(parent[node]!=-1):
                graph[parent[node]].append(node)

        max_longest = 1
        def dfs(node):

            nonlocal max_longest
            max1 = 0
            max2 = 0
            if(len(graph[node])==0):
                return 1

            for nbr in graph[node]:
                curr_max = dfs(nbr)
                if(s[nbr]==s[node]):
                    continue
                if(curr_max>max1):
                    max2 = max1
                    max1 = curr_max
                elif(curr_max>max2):
                    max2 = curr_max
                    
            max_longest = max(max_longest,max1+max2+1)     
            return max1+1
        dfs(0)
        return max_longest
