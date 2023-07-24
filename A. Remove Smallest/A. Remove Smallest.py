test_cases = int(input())
for i in range(test_cases):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()

    is_possible = True
    for i in range(n-1):
        if(abs(arr[i+1]-arr[i]>1)):
            is_possible=False
            break
    
    if(is_possible):
        print('YES')
    else:
        print('NO')
