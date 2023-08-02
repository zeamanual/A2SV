class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = defaultdict(set)

        for node1,node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        visited = set()
        label_stat = dict()
        def dfs(node):
            nonlocal visited
            nonlocal label_stat
            
            visited.add(node)

            curr_stat = defaultdict(int)

            for nbr in graph[node]:
                if(nbr not in visited):
                    sub_tree_stat =  dfs(nbr)

                   # maximum 26 iterations
                    for label in sub_tree_stat.keys():
                        curr_stat[label]+=sub_tree_stat[label]

            curr_stat[labels[node]]+=1
            label_stat[node]=curr_stat[labels[node]]
            return curr_stat

        dfs(0)
        answer=[]
        for i in range(n):
            answer.append(label_stat[i])
        return answer
