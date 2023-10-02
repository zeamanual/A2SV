class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.indices = dict()
        for index,word in enumerate(words):
            self.trie.insert(word,index)
            self.indices[word]=index
        

    def f(self, pref: str, suff: str) -> int:
        matching_words = self.trie.get_children(pref)
        max_idx = -1
        for word in matching_words:
            if suff == word[1][-len(suff):]:
                max_idx = max(max_idx, self.indices[word[1]])
        return max_idx


class TrieNode:
    def __init__(self,value='',index=0):
        self.is_end = False
        self.children = dict()
        self.value = value
        self.index = index

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str,word_index) -> None:

        curr_node =self.root
        for index in range(len(word)):
            
            if(word[index] not in curr_node.children):
                curr_node.children[word[index]] = TrieNode()

            curr_node = curr_node.children[word[index]]

        curr_node.value = word
        curr_node.index = word_index
        curr_node.is_end = True
                

    def startsWith(self, prefix: str):

        currNode = self.root

        for index in range(len(prefix)):
            if(prefix[index] not in currNode.children):
                return None
            
            currNode = currNode.children[prefix[index]]
            
        return currNode


    def get_children(self,word):

        node = self.startsWith(word)

        answer = []
        if(not node):
            return answer

        que = deque([node])

        while que:
            curr = que.popleft()
            if(curr.is_end):
                answer.append([curr.index,curr.value])
            for key in curr.children.keys():
                if(curr.children[key]):
                    que.append(curr.children[key])

        return answer



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
