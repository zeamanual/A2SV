class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()

        for word in words:
            trie.insert(word)


        answer = []
        for word in words:

            curr_answer = 0
            curr_node = trie.root
            for char in word:

                curr_node = curr_node.children[ord(char)-97]
                curr_answer+= trie.children_count(curr_node)

            answer.append(curr_answer)

        return answer
        




class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count=0
        self.prefix_count=0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr_node =self.root
        for index in range(len(word)):
            
            if(not curr_node.children[ord(word[index])-97]):
                curr_node.children[ord(word[index])-97] = TrieNode()

            curr_node = curr_node.children[ord(word[index])-97]
            curr_node.prefix_count+=1

        curr_node.is_end = True
        curr_node.count+=1


    def search(self, word: str) -> bool:

        currNode = self.root

        for index in range(len(word)):

            if(not currNode.children[ord(word[index])-97]):
                return False
            currNode = currNode.children[ord(word[index])-97]
            
        if(not currNode.is_end):
            return False
        
        return True
                

    def startsWith(self, prefix: str):

        currNode = self.root

        for index in range(len(prefix)):
            if(not currNode.children[ord(prefix[index])-97]):
                return None
            
            currNode = currNode.children[ord(prefix[index])-97]
            
        return currNode

    def children_count(self,node):

        if not node:
             return 0

        return node.prefix_count
