# Enter your code here. Read input from STDIN. Print output to STDOUTlet 
inputCount = int(input())
words = {}

for i in range(inputCount):
    currentWord = input()
    if(words.get(currentWord)!=None):
        words[currentWord]+=1
    else:
        words[currentWord]=1
        
print(len(words))
for key in words.keys():
    print(words[key],end=' ')
