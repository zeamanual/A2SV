import math
test_cases = int(input())
 
for count in range(test_cases):
    x = int(input())
 
    if(x==1):
        print(3)
    elif( x%2==0 and math.log2(x)== math.floor(math.log2(x))):
        print(x+1)
    elif(x%2==0):
        print(x-(x&(x-1)))
    else:
        print(1)
