# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n,m=list(map(int,input().split(' ')))

letter_dic = defaultdict(list)

for index in range(n):
    letter = input()
    letter_dic[letter].append(f"{index+1}")

for i in range(m):
    letter = input()
    if(letter in letter_dic):
        print(" ".join(letter_dic[letter])) 
    else:
        print('-1')
