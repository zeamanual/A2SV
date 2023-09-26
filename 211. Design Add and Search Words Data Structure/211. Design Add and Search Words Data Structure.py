class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr_node =self.root
        for index in range(len(word)):
            
            if(not curr_node.children[ord(word[index])-97]):
                curr_node.children[ord(word[index])-97] = TrieNode()

            curr_node=curr_node.children[ord(word[index])-97]

        curr_node.is_end = True

    def search(self, word: str,root=None) -> bool:

        if(not root):
            root = self.root

        currNode = root
        for index in range(len(word)):
            if(not word[index].isalpha()):

                possible_answers = [ self.search(word[index+1:],currNode.children[i]) if currNode.children[i] else False for i in range(26)]
                return any(possible_answers)

            if(not currNode.children[ord(word[index])-97]):
                return False
            currNode = currNode.children[ord(word[index])-97]
            
        if(not currNode.is_end):
            return False
        
        return True 

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
