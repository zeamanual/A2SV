class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        trie = Trie()
        trie.insert(s)
        count =0
        cache=dict()

        for word in words:
            if(word in cache):
                count+=1 if cache[word] else 0
            else:
                cache[word]=trie.search(word)
                count+=1 if cache[word] else 0

        return count       


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        curr_node =self.root
        for index in range(len(word)):
            if( word[index] not in curr_node.children):
                curr_node.children[word[index]] = TrieNode()

            curr_node=curr_node.children[word[index]]

        curr_node.is_end = True


    def search(self, word: str) -> bool:

        currNode = self.root

        index=0
        while(index<len(word) and len(currNode.children.keys())>0):
            if( word[index] in currNode.children):
                index+=1

            currNode = currNode.children[list(currNode.children.keys())[0]]
        
        return index==len(word)
