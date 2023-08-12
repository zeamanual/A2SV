class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        stat = [i for i in range(len(s))]

        def get_rep(node):
            rep = stat[node]
            if(rep !=node):
                stat[node] = get_rep(rep)
            return stat[node] 

        def union(node1, node2):
            node1_rep = get_rep(node1)
            node2_rep = get_rep(node2)
            if(node1_rep!=node2_rep):
                stat[node1_rep]=node2_rep

        for pair in pairs:
            union(pair[0],pair[1])

        hash_map = defaultdict(set)
        for pair in pairs:
            rep = get_rep(pair[0])
            hash_map[rep].add(pair[0])
            hash_map[rep].add(pair[1])
        
        for key in hash_map.keys():
            group_index = list(hash_map[key])
            group_char = [s[i] for i in group_index]
            group_index.sort()
            group_char.sort()
            counter = 0
            s = list(s)
            for index in group_index:
                s[index]=group_char[counter]
                counter+=1

        return ''.join(s)
