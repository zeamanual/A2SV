class MapSum:

    def __init__(self):
        self.trie = Trie()
        self.data = dict()
        

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key)
        self.data[key]=val
        

    def sum(self, prefix: str) -> int:

        keys = self.trie.match(prefix)
        answer = 0
        for key in keys:
            answer+=self.data[key]

        return answer

        

class TrieNode:
    def __init__(self,value=''):
        self.is_end = False
        self.children = dict()
        self.value = value

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        print('insert',word)
        curr_node =self.root
        for index in range(len(word)):
            if( word[index] not in curr_node.children):
                curr_node.children[word[index]] = TrieNode()

            curr_node=curr_node.children[word[index]]

        curr_node.is_end = True
        curr_node.value = word


    def search(self, word: str):

        currNode = self.root

        for index in range(len(word)):

            if( word[index] not in currNode.children):
                return None
            
            currNode = currNode.children[word[index]]
            
        return currNode

    def match(self,prefix):

        startingNode = self.search(prefix)

        if(not startingNode):
            return []
        else:

            answer =[]
            que = deque([startingNode])

            while(que):

                currNode=que.popleft()

                if(currNode.is_end):
                    answer.append(currNode.value)
                
                for key in currNode.children.keys():
                    que.append(currNode.children[key])

            return answer


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
