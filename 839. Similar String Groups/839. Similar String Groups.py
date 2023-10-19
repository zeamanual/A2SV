class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        parent = dict()
        rank = defaultdict(lambda : 1)
        def union(word1,word2):
                word1_rep = get_rep(word1)
                word2_rep = get_rep(word2)
                
                if(word1_rep==word2_rep):
                    return
                if(rank[word1_rep]<rank[word2_rep]):
                    parent[word1_rep]=word2_rep
                elif(rank[word1_rep]<rank[word2_rep]):
                    parent[word2_rep]=word1_rep
                else:
                    parent[word1_rep]=word2_rep
                    rank[word2_rep]+=1

        def get_rep(word):

            if(word in parent):
                if(parent[word]!=word):
                    parent[word]=get_rep(parent[word])
            else:
                parent[word]=word

            return parent[word]

        def is_similar(word1,word2):
            diff =0
            for index in range(len(word1)):
                if(word1[index]!=word2[index]):
                    diff+=1

            return diff<=2

        for i in range(len(strs)):
            for  j in range(i+1,len(strs)):
                if(is_similar(strs[i],strs[j])):
                    union(strs[i],strs[j])
                    
        unique = set()
        for string in strs:
            unique.add(get_rep(string))
        return  len(unique)
