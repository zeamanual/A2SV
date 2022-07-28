class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        sentence = []
        for i in range(len(words)):
            sentence.append(None)
            
        for word in words:
            sentence[int(word[-1])-1]=word[0:-1]
        sentence = ' '.join(sentence)
        return sentence
            
        
