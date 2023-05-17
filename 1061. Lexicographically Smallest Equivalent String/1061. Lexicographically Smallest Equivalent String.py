class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        stat = defaultdict(str)
        for i in range(26):
            stat[chr(97+i)] = chr(97+i)

        def get_rep(node):
            rep = stat[node]
            while(rep!=node):
                node = stat[rep]
                rep = stat[node]
            return rep

        def union(node1, node2):
            node1_rep = get_rep(node1)
            node2_rep = get_rep(node2)
            if(node1_rep>node2_rep):
                stat[node1_rep]=node2_rep
            else:
                stat[node2_rep]=node1_rep

        for i in range(len(s1)):
            union(s1[i],s2[i])  
        answer = ''
        for char in baseStr:
            answer+=get_rep(char)

        return answer
