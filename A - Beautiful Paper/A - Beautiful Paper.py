test_cases = int(input())
 
for count in range(test_cases):
    size11,size12 = list(map(int,input().split()))
    size21,size22 = list(map(int,input().split()))
 
    if(size11==size21 and size11== (size12 +size22)):
        print('Yes')
    elif(size11==size22 and size11== (size12 +size21)):
        print('Yes')
    elif(size12==size21 and size12== (size11 +size22)):
        print('Yes')
    elif(size12==size22 and size12== (size11 +size21)):
        print('Yes')
    else:
        print('No')
